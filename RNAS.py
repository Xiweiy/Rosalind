##Wobble Bonding and RNA Secondary Structures
##http://rosalind.info/problems/rnas/

from numpy import array
import sys
sequence = "AGUACUUACUCUCUUACACCAAUGUAACGCGGCCGCUCUUAUGUACGGGUCUCUUAGAACCCUAAAAUUAGAUGGGCGGCGAAUCCAUACGCGGUCCUCCAGGGUCUGCGUGGCGACUACACCAGAGGAAACAACCCUCGACGAUCGUAUUUCACUAAAUAACUCGCUCACAGUAUUUUCCUCAUCGUCCAU"
n = len(sequence)
allpositions = {"A":[],"U":[],"C":[],"G":[]}
for i in range(len(sequence)):
      allpositions[sequence[i]].append(i)

def separate_before_after(positions,position):
      number = {}
      before = {}
      after = {}
      for i in positions:
            if positions[i] == []:
                  number[i]= 0
                  before[i] = []
                  after[i] = []
            elif position < positions[i][0]:
                  number[i] = -1
                  before[i] = []
                  after[i] = positions[i]
            elif position >= positions[i][-1]:
                  number[i] = len(positions[i])
                  before[i] = positions[i]
                  after[i] = []
            ##Binary search
            else:
                  low = 0
                  high = len(positions[i])-1
                  middle = (low + high)/2
                  while middle - low >0:                        
                        if position < positions[i][middle]:
                              high = middle
                              middle = (low + high)/2 
                        else:
                              low = middle
                              middle = (low + high)/2
                  number[i] = middle
                  before[i] = positions[i][:middle+1]
                  after[i] = positions[i][middle+1:]
      return before,after
      
complementary = {"A":["U"],"U":["A", "G"],"G":["C", "U"],"C":["G"]}           
memory = array([[-1L]*n]*n, dtype = object)
########Important to set array type to object, so that the array can contain any arbitrary data type, can be an int much larger than sys.maxint

def count_pair(start,end,locations):
      if memory[start,end] != -1:
            return memory[start,end]
      ##Set the smallest situations differently
      elif end-start <4:
            return 1L
      elif end-start ==4:
            if sequence[start] in complementary[sequence[end]]:
                  memory[start,end] = 2L
                  return 2L
            else:
                  memory[start,end] = 1L
                  return 1L
      else:
            ## subset the list and call the function again
            pair = complementary[sequence[start]]
            count = 0L
            combined_locations = []
            for i in pair:
                  for j in locations[i]:
                        if j >= start+4:
                              combined_locations.append(j)
            for i in combined_locations:
                  before,after = separate_before_after(locations,i)[:]
                  before[sequence[start]] = before[sequence[start]][1:]
                  before[sequence[i]]= before[sequence[i]][:-1]
                  if i - start ==1:
                        before = []
                        before_num = 1L
                        after_num = count_pair(i+1,end,after)
                  elif end == i:
                        before_num = count_pair(start+1,i-1,before)
                        after = []
                        after_num = 1L
                  else:
                        before_num = count_pair(start+1,i-1,before)
                        after_num = count_pair(i+1,end,after)
                  count = count + before_num * after_num
      ## Calculate the crossing between start+1 : end
            notinvolved_positions = {i:locations[i] for i in locations}
            if len(locations[sequence[start]]) ==1:
                  notinvolved_positions[sequence[start]] = []
            else:
                  notinvolved_positions[sequence[start]] = locations[sequence[start]][1:]
            notinvolved = count_pair(start+1,end, notinvolved_positions)
            memory[start,end] = (count + notinvolved)
      return memory[start,end]
print count_pair(0,n-1,allpositions)
