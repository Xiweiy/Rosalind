##Counting Unrooted Binary Trees
##http://rosalind.info/problems/cunr/`


#An unrooted binary tree on n leaves has 2n-3 edges and n-2 internal nodes
#let u(n) be the number of unrooted trees with n labeled leaves
#given an unrooted tree with n leaves, an extra leaf can be added on any branch to make a tree with (n+1) leaves

#n leves --> 2n-3 possible branches
#==> U(n+1) = (2n-3)U(n)  ==> U(n) = (2n-5)!!

n = 835
recur = 2*n-5
product = 1
while recur >1:
      product = recur*product %1000000
      recur -= 2
print product
