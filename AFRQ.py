##Counting Disease Carriers
##http://rosalind.info/problems/afrq/

infile = open('rosalind_afrq.txt','r')
homo = infile.readlines()[0].rstrip('\n')

#homo = '0.1 0.25 0.5'
homo = [float(i) for i in homo.split(' ')]

for i in homo:
      recessive = i**.5
      dominant = 1- recessive
      print round(2*recessive*dominant +i,3),
