##Finding a Shared Spliced Motif

"""motiffile = open("rosalind_lcsq.txt","r")
motiflist = motiffile.readlines()
motiflist = ("".join([i.rstrip("\n") for i in motiflist])).split(">")[1:]


sequence1 = motiflist[0][13:]
sequence2 = motiflist[1][13:]"""

sequence1 = "ATCTGAT"
sequence2 = "TGCATA"
m = len(sequence1)
n = len(sequence2)

import numpy
sublen = numpy.matrix([[0]*m]*n)
traceback = numpy.array([[{"a":-1,"b":-1}]*m]*n)

##Initialize the first row and first column
for i in range(0,m):
      if sequence1[i]==sequence2[0]:
            break
sublen[0,i:] = 1
traceback[0,i+1:] = [{"a":0,"b":j} for j in range(i,m-1)]

for i in range(0,n):
      if sequence2[i]==sequence1[0]:
            break
sublen[i:,0] = 1
traceback[i+1:,0] = [{"a":j,"b":0} for j in range(i,n-1)]

##store the last position of ATCG's
lastATCG = [{"A":-1,"T":-1,"C":-1,"G":-1}]
for i in range(0,n):
      lastATCG[i][sequence2[i]] = i
      lastATCG.append(lastATCG[i].copy())
      
for i in range(1,n):
      for j in range(1,m):
            lastaligned = lastATCG[i][sequence1[j]]
            if lastaligned < 0:
                  newlength = 0
            elif lastaligned == 0:
                  newlength = 1
            else:
                  newlength = sublen[lastaligned-1,j-1] + 1
            if newlength > sublen[i,j-1]:
                  sublen[i,j] = newlength
                  traceback[i,j] = {"a": lastaligned-1, "b": j-1}
            else:
                  sublen[i,j] = sublen[i,j-1]
                  traceback[i,j] = {"a":i, "b":j-1}

currenta=n-1
currentb=m-1
nextstate = traceback[n-1,m-1]
nexta=nextstate["a"]
nextb=nextstate["b"]
subseq = []
while nexta!=-1 and nextb!=-1: 
      if currenta == nexta or currentb == nextb:
            pass
      else:
            subseq.append(sequence2[nexta+1])
            #print nextstate
      currenta = nexta
      currentb = nextb
      nextstate = traceback[currenta,currentb]
      nexta=nextstate["a"]
      nextb=nextstate["b"] 
if nexta==-1 or nextb == -1 and sequence1[nextb+1] ==sequence2[nexta+1]:
      subseq.append(sequence1[nextb+1])
subseq = "".join(subseq[::-1])
