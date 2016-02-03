##Finding Disjoint Motifs in a Gene
##http://rosalind.info/problems/itwv/


##reduce calculation by segmenting the long sequence of S into fragment no larger than the total motif size
##and hence eliminate the long time spent on the triple for loop in the find_allpos function
##since any index list with range > total size of motifs will be invalid

S = 'GACCACGGTT'
motif = ['ACAG','GT','CCG']

inputfile = open('rosalind_itwv.txt','r')
inputlist = inputfile.readlines()
S = inputlist[0].rstrip('\n')
motif = [i.rstrip('\n') for i in inputlist[1:]]
n = len(motif)


##Find locations of each nucleotide
def find_letter_pos(pattern):
      dic = {'A':[], 'C':[], 'G':[], 'T':[]}
      for i in range(len(pattern)):
            letter = pattern[i]
            dic[letter].append(i)
      return dic

def find_allpos(motif, dic):
      m = len(motif)
      listindex = [[i] for i in dic[motif[0]]]
      for i in motif[1:]:
            listindex = [k+[j] for j in dic[i] for k in listindex if j>k[-1]]
      return listindex

def check_interwoven(motifi, motifj, dic):
      m = len(motifi)
      n = len(motifj)
      listi= find_allpos(motifi, dic)
      listj= find_allpos(motifj, dic)
      for i in listi:
            for j in listj:
                  combined = sorted(set(i+j))
                  if len(combined) == m+n and combined[-1]-combined[0] == m+n-1:
                        return 1
      return 0

def output_interwoven(motifi, motifj, S):
      m = len(motifi)
      n = len(motifj)
      dic = find_letter_pos(S[:m+n])
      if check_interwoven(motifi, motifj, dic):
            return 1

      ##to avoid run find_letter_pos() function with O(len(S)) times
      ##we only need roughly O(1) on updating dic
      
      for i in range(len(S)-m-n):
            dic[S[i]].pop(0)
            dic[S[i+m+n]].append(i+m+n)
            if check_interwoven(motifi, motifj, dic):
                  return 1
      return 0


from numpy import array
from pandas import DataFrame
matrix = array([[-1]*n]*n)
for i in range(n):
      for j in range(n):
            if matrix[i,j] == -1:
                  matrix[i,j]= matrix[j,i]= output_interwoven(motif[i],motif[j], S)

matrix = DataFrame(matrix)
print matrix.to_string(index=False)
