##Matching a Spectrum to a Protein
##http://rosalind.info/problems/prsm/

n=4
strings = ['GSDMQS','VWICN','IASWMQS','PVSMGAD']
R = [445.17838,115.02694,186.07931,314.13789,317.1198,215.09061]

Monoisotopic = {'A':'71.03711','C':'103.00919','D':'115.02694','E':'129.04259',
'F':'147.06841','G':'57.02146','H':'137.05891','I':'113.08406','K':'128.09496',
'L':'113.08406','M':'131.04049','N':'114.04293','P':'97.05276','Q':'128.05858',
'R':'156.10111','S':'87.03203','T':'101.04768','V':'99.06841','W':'186.07931',
'Y':'163.06333'}

from decimal import Decimal

infile = open('rosalind_prsm.txt','r')
inlist = infile.readlines()
n = int(inlist[0].rstrip('\n'))
strings = [i.rstrip('\n') for i in inlist[1:n+1]]
R = [Decimal(i.rstrip('\n')) for i in inlist[n+1:]]

MULTISETS = []
for each_string in strings:
      growing_total = []
      total = 0
      for each_residual in each_string:
            total += Decimal(Monoisotopic[each_residual])
            growing_total.append(total)
      multiset = []
      for i in growing_total[:-1]:
            multiset += [i, total-i]
      MULTISETS.append(multiset)
      
maxcount = 0
x = ''
for i in range(len(strings)):
      spec1 = MULTISETS[i]
      R_Sk = {}
      for m in spec1:
            for n in R:
                  diff = str(float(m-n))
                  if diff in R_Sk:
                        R_Sk[diff] +=1
                  else:
                        R_Sk[diff] = 1
                  if R_Sk[diff] > maxcount:
                        maxcount = R_Sk[diff]
                        x = strings[i]
                        Rs = R_Sk
print maxcount
print x

##NOTE: the inaccurate representation of float may raise a problem as substraction between
##two identical floats may be a positive/negative super small number, and rounding
##cannot solve the problem with positive/negative sign
##Use of the decimal function can solve this, but lead to a significantly
##longer time.
      
