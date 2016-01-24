##Inferring protein from spectrum

L = [3524.8542,3710.9335,3841.974,3970.0326,4057.0646]

infile = open('rosalind_spec.txt', 'r')
L = [float(i.rstrip('\n')) for i in infile.readlines()]

Mass = [57.02146,71.03711,87.03203,97.05276,99.06841,101.04768,103.00919,
        113.08406,114.04293,115.02694,128.05858,128.09496,129.04259,131.04049,
        137.05891,147.06841,156.10111,163.06333,186.07931]
AA = ['G','A','S','P','V','T','C','I','N','D','Q','K','E','M','H','F','R','Y','W']

D = [L[i]-L[i-1] for i in range(1,len(L))]

seq = ''
for i in D:
      index = 0
      mindiff = 1000
      curdiff = abs(i - Mass[index])
      while curdiff < mindiff:
            index +=1
            mindiff = curdiff
            if index > 18:
                  break
            else:
                  curdiff = abs(i - Mass[index])           
      seq += AA[index-1]
print seq
