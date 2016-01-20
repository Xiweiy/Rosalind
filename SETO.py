##Introduction to Set Operations

n = 10
a = '{1, 2, 3, 4, 5}'
b = '{2, 8, 5, 10}'

inputfile = open('rosalind_seto.txt','r')
inputlist = inputfile.readlines()
n = int(inputlist[0].rstrip('\n'))
a = inputlist[1].rstrip('\n')
b = inputlist[2].rstrip('\n')


a = a.lstrip('{').rstrip('}').split(',')
b = b.lstrip('{').rstrip('}').split(',')

a = {int(i):0 for i in a}
b = {int(i):0 for i in b}

AUB = []
ANB = []
A_B = []
B_A = []
AC = []
BC = []
for i in range(1,n+1):
      if i in a and i in b:
            AUB.append(i)
            ANB.append(i)
      elif i in a:
            AUB.append(i)
            A_B.append(i)
            BC.append(i)
      elif i in b:
            AUB.append(i)
            B_A.append(i)
            AC.append(i)
      else:
            AC.append(i)
            BC.append(i)

def printset(outputset):
      outputset = str(outputset).lstrip('[').rstrip(']')
      outputset = '{' + outputset + '}'
      return outputset

print printset(AUB)
print printset(ANB)
print printset(A_B)
print printset(B_A)
print printset(AC)
print printset(BC)
