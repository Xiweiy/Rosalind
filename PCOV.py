##Genome Assembly with Perfect Coverage
##http://rosalind.info/problems/pcov/

kmers = ['ATTAC','TACAG','GATTA','ACAGA','CAGAT','TTACA','AGATT']
infile = open('rosalind_pcov.txt','r')
kmers = [i.rstrip('\n') for i in infile.readlines()]

k = len(kmers[0])
dic = {}
for i in kmers:
      dic[i[1:]] = ''
      
for i in kmers:
      dic[i[:-1]] = i

string = dic.keys()[0]
curkey = string
while len(dic):
      #print curkey
      curvalue = dic[curkey]
      string += curvalue[-1]
      dic.pop(curkey)
      curkey = curvalue[1:]
print string[k-1:]
