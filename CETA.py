##Counting Optimal Alignments
##http://rosalind.info/problems/ctea/


import sys
sys.setrecursionlimit(70000)  ##allocate memory to avoid exceeding maximum recursion depth

##NOTE: minimizing edit distance is not always the same senario as maximizing matching sequence
##In this case, minimizing edit distance is required
seq1 = 'PLEASANTLY'
seq2 = 'MEANLY'

inputfile = open('rosalind_ctea.txt','r')
inputlist = inputfile.readlines()
inputlist = ("".join([i.rstrip("\n") for i in inputlist])).split(">")
seq1 = inputlist[1][13:]
seq2 = inputlist[2][13:]

m = len(seq1)
n = len(seq2)


##keep track of number of aligned sequences in local fragments (avoid repeated calculation)
class TraceEdge:
      def __init__(self):
            self.previous = [[-1,-1]]
            self.count = 0

import numpy
scores = numpy.matrix([[0]*(m+1)]*(n+1))  ##put one more row/column since easy to initialize

##Initialize first row and first column
scores[0,:] = range(m+1)
scores[:,0] = numpy.reshape(range(n+1),(n+1,1))

traceback = numpy.array([[TraceEdge() for i in range(m+1)] for j in range(n+1)])

print m,n
##Scan through each row
for i in range(1,n+1):
      for j in range(1,m+1):
            extend = 0
            if seq2[i-1] != seq1[j-1]:
                  extend = 1
            curscore = [scores[i-1,j-1]+extend, scores[i-1,j]+1, scores[i,j-1]+1]
            prev = [[i-1,j-1],[i-1,j],[i,j-1]]
            scores[i,j] = min(curscore)
            traceback[i,j].previous = [prev[k] for k in range(3) if curscore[k] ==scores[i,j]]            

def count_traceback(row, col):
      if not (row and col):
            return 1
      if traceback[row,col].count:
            return traceback[row,col].count
      prevsteps = traceback[row,col].previous
      count = 0
      for each_prev in prevsteps:
            next_row, next_col = each_prev
            count += count_traceback(next_row, next_col)
      traceback[row,col].count = count
      return count %134217727

print count_traceback(i,j)% 134217727



##################Method 2: Iterative ############################################################

#while i and j:
      
