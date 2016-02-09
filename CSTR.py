##Creating a Character Table from Genetic Strings
##http://rosalind.info/problems/cstr/

##read fixed width file
#import pandas
#infile = pandas.read_fwf('practice.txt', widths = [1]*8, header=None, engine='python')

infile = open('rosalind_cstr.txt','r')
strings = [i.rstrip('\n') for i in infile.readlines()]
m,n = len(strings[0]), len(strings)

for i in range(m):
      dic = {}
      for j in strings:
            dic[j[i]] = dic[j[i]]+1 if j[i] in dic else 1
      if len(dic) == 2 and min(dic.values())>1:
            label = ''
            for j in strings:
                  label += str(dic.keys().index(j[i]))
            print label
                  
            
            

