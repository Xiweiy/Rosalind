##Interleaving two motifs
#use alignment

inputfile = open('rosalind_scsp.txt','r')
inputlist = inputfile.readlines()
seq1 = inputlist[0].rstrip('\n')
seq2 = inputlist[1].rstrip('\n')

m = len(seq1)
n = len(seq2)
from numpy import array
scores = array([[0]*m]*n)

##initiate the first row and first column
for i in range(m):
      if seq2[0]== seq1[i]:
            scores[0,i] = 1
for i in range(n):
      if seq1[0]==seq2[i]:
            scores[i,0] = 1

traceback = array([[(-1,-1)]*m]*n)
for i in range(1,n):
      for j in range(1,m):
            aligned=0
            if seq2[i] == seq1[j]:
                  aligned =1
            comparescore = {scores[i-1,j-1]+aligned : [i-1, j-1], scores[i-1,j]: [i-1,j],
                            scores[i, j-1]:[i, j-1]}
            scores[i,j]=max(comparescore.keys())
            traceback[i,j] = comparescore[scores[i,j]]
alignment = ''
while i and j:
      #print traceback[i,j]
      if list(traceback[i,j]) == [i-1,j-1]:
            alignment = seq1[j] + alignment
      elif list(traceback[i,j]) == [i-1, j]:
            alignment = seq2[i] + alignment
      elif list(traceback[i,j]) == [i, j-1]:
            alignment = seq1[j] + alignment
      i,j = traceback[i,j]

if i:
      alignment = seq2[:i+1]+alignment
if j:
      alignment = seq1[:j+1]+alignment
      
print alignment
