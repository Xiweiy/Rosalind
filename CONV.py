##Comparing Spectra with the Spectral Convolution

spec1 = '186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544'
spec2 = '101.04768 158.06914 202.09536 318.09979 419.14747 463.17369'

infile = open('rosalind_conv.txt','r')
spec1, spec2 = infile.readlines()

spec1 = [float(i) for i in spec1.rstrip('\n').split(' ')]
spec2 = [float(i) for i in spec2.rstrip('\n').split(' ')]

S1_S2 = {}
maxcount = 0
x = ''
for i in spec1:
      for j in spec2:
            diff = str(i-j)  ##convert to string because the numeric keys in dictionary tend to change by small amount
            if diff in S1_S2:
                  S1_S2[diff] +=1
            else:
                  S1_S2[diff] = 1
            if S1_S2[diff] > maxcount:
                  maxcount = S1_S2[diff]
                  x = diff
print maxcount
print x
