##Edit Distance Alignment
##http://rosalind.info/problems/edta/


##NOTE: minimizing edit distance is not always the same senario as maximizing matching sequence
##In this case, minimizing edit distance is required
seq1 = 'PRETTY'
seq2 = 'PRTTEIN'

inputfile = open('rosalind_edta.txt','r')
inputlist = inputfile.readlines()
inputlist = ("".join([i.rstrip("\n") for i in inputlist])).split(">")
seq1 = inputlist[1][13:]
seq2 = inputlist[2][13:]

m = len(seq1)
n = len(seq2)

import numpy
scores = numpy.matrix([[0]*(m+1)]*(n+1))  ##put one more row/column since easy to initialize

##Initialize first row and first column
scores[0,:] = range(m+1)
scores[:,0] = numpy.reshape(range(n+1),(n+1,1))

traceback = numpy.array([[(-1,-1)]*(m+1)]*(n+1))

##Scan through each row
for i in range(1,n+1):
      for j in range(1,m+1):
            extend = 0
            if seq2[i-1] != seq1[j-1]:
                  extend = 1
            comparescore = {scores[i-1,j-1]+extend:[i-1,j-1],
                            scores[i-1,j]+1:[i-1,j],
                            scores[i,j-1]+1:[i,j-1]}
            scores[i,j] = min(comparescore.keys())
            traceback[i,j] = comparescore[scores[i,j]]           


alignment1 = ''
alignment2 = ''
mismatch = 0
while i and j:
      #print traceback[i,j]
      nexti,nextj = traceback[i,j]
      if list(traceback[i,j]) == [i-1,j-1]:
            alignment1 = seq1[j-1] + alignment1
            alignment2 = seq2[i-1] + alignment2
      elif list(traceback[i,j]) == [i-1, j]:
            alignment1 = '-' + alignment1
            alignment2 = seq2[i-1] + alignment2
      elif list(traceback[i,j]) == [i, j-1]:
            alignment1 = seq1[j-1] + alignment1
            alignment2 = '-' + alignment2
      if alignment1[0] != alignment2[0]:
            mismatch += 1
      if '-' not in [alignment1[0],alignment2[0]]:
            i,j = i-1,j-1
      else:
            i,j = traceback[i,j]


if i:
      alignment2 = seq2[:i]+alignment2
      alignment1 = '-'*i + alignment1
      mismatch += i
elif j:
      alignment1 = seq1[:j]+alignment1
      alignment2 = '-'*j + alignment2
      mismatch += j

print mismatch      
print alignment1
print alignment2

