##Independent Segregation of Chromosomes
##http://rosalind.info/problems/indc/

from math import factorial,log

def combinatorial(total, sample):
      return factorial(total)*1.0/factorial(sample)/factorial(total-sample)

n = 44

A = []
grow = 0
denom = 2**(2*n)
for i in range(2*n):
      factor = combinatorial(2*n,i)
      prob = factor/denom
      grow += prob
      A = [log(grow, 10)] + A

for i in A:
      print round(i,3),
