##Sorting by Reversals

seq1 = '1 2 3 4 5 6 7 8 9 10'
seq2 = '1 8 9 3 2 7 6 5 4 10'

infile = open('rosalind_sort.txt', 'r')
seq1, seq2 = infile.readlines()

seq1 = [int(i) for i in seq1.rstrip('\n').split(' ')]
seq2 = [int(i) for i in seq2.rstrip('\n').split(' ')]

n = len(seq1)
positions = {seq1[i]:i for i in range(n)}
seq2ind = [-1] + [positions[i] for i in seq2] + [10]

from itertools import combinations

class permutations:
      def __init__(self, string, step, reversions):
            self.string = string
            self.breakpoints = []
            self.nbk = 0
            self.step = step    # of reversion needed
            self.reversions = reversions   #each reversion step

      def count_breakpoints(self):
            self.breakpoint = []
            self.nbk = 0
            for i in range(len(self.string)-1):
                  if abs(self.string[i+1]-self.string[i])> 1:
                        self.breakpoints.append(i+1)
                        self.nbk += 1
            

##For each permutations and its breakpoints, return a list of new permutations and new breakpoints after reversions
def one_reverse(oneperm):
      new_perms = []
      oldstring = oneperm.string
      bklist = combinations(oneperm.breakpoints, 2)  #list of all reversal indices pairs
      bkpt_reduce = 1
      for each_break in bklist:
            i,j = each_break
            if j - i > 1:    #have to reverse a fragment with length >1, otherwise will return identical sequence
                  newstring = oldstring[:i] + oldstring[j-1:i-1:-1] + oldstring[j:]
                  newperm = permutations(newstring, oneperm.step+1, oneperm.reversions + [[i,j-1]])
                  newperm.count_breakpoints()
                  ####There are special cases that even if the 2 ends after reversion are continuous,
                  ####the number of breakpoints did not reduce by 2. Since the former string may already be continuous at one end
                  ####Has to use count_breakpoints() everytime                      

                  if not newperm.nbk:
                        return [newperm]
                  elif oneperm.nbk - newperm.nbk > bkpt_reduce:
                        new_perms = [newperm]
                        bkpt_reduce = oneperm.nbk - newperm.nbk
                  elif oneperm.nbk - newperm.nbk == bkpt_reduce:
                        new_perms.append(newperm)
                  ##return the list with largest reduction in # of breakpoint
      return new_perms                                          


##Initialize the starting permutation -- seq2ind
startperm = permutations(seq2ind, 0, [])
startperm.count_breakpoints()
curlist = [startperm]    

##Similar to BFS in graph -- greedy algm that find the best solution at each step
def reversal_distance(permlist):
      newperms = []
      minnbk = 20
      for each_perm in permlist:           
            if not each_perm.nbk:
                  return [each_perm]
            ##Else generate all the permutations after one reversion
            newperm = one_reverse(each_perm)  ##this function increment step by 1 and incorporate the reversion step
            newperms += newperm
      for i in newperms:
            if i.nbk < minnbk:
                  minperms = [i]
                  minnbk = i.nbk
            elif i.nbk == minnbk:
                  minperms += [i]            
      while minperms[0].nbk:
            minperms = reversal_distance(minperms)
      #minperms is the list of reversions with max reduction in # breakpoints, after combining the reversed string from each element in the list
      
      return minperms

final =  reversal_distance(curlist)[0]
print final.step
for i in final.reversions[::-1]:
      for j in i:
            print j,
      print
