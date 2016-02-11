##Global Alignment with Scoring Matrix
##http://rosalind.info/problems/glob/

import pandas
from pandas import DataFrame

BLOSUM = pandas.read_table('BLOSUM62.txt', delim_whitespace=True)
seq1 = 'PLEASANTLY'
seq2 = 'MEANLY'

inputfile = open('rosalind_glob.txt','r')
inputlist = inputfile.readlines()
inputlist = ("".join([i.rstrip("\n") for i in inputlist])).split(">")
seq1 = inputlist[1][13:]
seq2 = inputlist[2][13:]

m = len(seq1)
n = len(seq2)
from numpy import array
scores = array([[0]*m]*n)

##initiate the first row and first column
for i in range(m):
      scores[0,i] = -5*i + BLOSUM[seq2[0]][seq1[i]]
for i in range(n):
      scores[i,0] = -5*i + BLOSUM[seq1[0]][seq2[i]]

for i in range(1,n):      
      for j in range(1,m):
            aligned = BLOSUM[seq2[i]][seq1[j]]
            comparescore = {scores[i-1,j-1]+aligned : [i-1, j-1], scores[i-1,j]-5: [i-1,j],
                            scores[i, j-1]-5:[i, j-1]}
            scores[i,j]=max(comparescore.keys())
