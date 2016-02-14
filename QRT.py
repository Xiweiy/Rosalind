##Quartets
##http://rosalind.info/problems/qrt/

species = ['cat', 'dog', 'elephant', 'ostrich', 'mouse', 'rabbit', 'robot']
table = ['01xxx00','x11xx00','111x00x']

infile = open('rosalind_qrt.txt','r')
inlist = infile.readlines()
species = inlist[0].rstrip('\n').split(' ')
table = [i.rstrip('\n') for i in inlist[1:]]

from itertools import combinations

outfile = open('result1.txt','w')
nspecies = len(species)
cache = {}   ##keep track of the existing split, to avoid repetition
for each_char in table:
      dic = {'1':[], '0':[]}
      for i in range(nspecies):
            if each_char[i] in dic:
                  dic[each_char[i]].append(i)
      if len(dic['1'])>1 and len(dic['0'])>1:
            taxa1 = list(combinations(dic['1'], r=2))
            taxa0 = list(combinations(dic['0'], r=2))
            for m in taxa1:
                  for n in taxa0:
                        if str([m,n]) not in cache and str([n,m]) not in cache:
                              cache[str([m,n])] = 0
                              outfile.write('{'+species[m[0]]+', '+species[m[1]]+'} '+'{'+species[n[0]]+', '+species[n[1]]+'}\n')
outfile.close()
            
            
