##Constructing a De Brujin Graph

dna = ['TGAT','CATG','TCAT','ATGC','CATC','CATC']


infile = open('rosalind_dbru.txt','r')
dna = [i.rstrip('\n') for i in infile.readlines()]
k = len(dna[0]) - 1

reverse_complementary={'A':'T', 'T':'A','G':'C','C':'G'}
def rev_comp(dnasequence):
      reverse_complement_sequence=""
      for i in dnasequence[::-1]:
          reverse_complement_sequence+=reverse_complementary[i]
      return reverse_complement_sequence

adjlist = []
for i in dna:
      rev = rev_comp(i)
      adjlist.append((i[:k],i[1:]))
      adjlist.append((rev[:k], rev[1:]))

##Set function to generate a set from a list
adjlist = set(adjlist)

outfile = open('results.txt','w')
for i in adjlist:
       outfile.write('(%s, %s)\n' %i)
outfile.close()


