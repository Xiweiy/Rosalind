##Distances in Trees
treefile = open("rosalind_nwck.txt","r")
treelist = treefile.readlines()
treelist = [i.rstrip("\n") for i in treelist]
tree = []
pair = []
for i in range(len(treelist)):
      if i %3 == 0:
            tree.append(treelist[i])
      elif i %3 ==1:
            pair.append(treelist[i])


def find_start(pair_of_nodes, one_tree):
      pair = pair_of_nodes.split()
      a = len(pair[0])
      b = len(pair[1])
      for i in range(len(one_tree)):
            if one_tree[i:i+a] == pair[0]:
                  return i,pair[1],b
            elif one_tree[i:i+b] == pair[1]:
                  return i, pair[0],a

##Strategy 1: keep track of the distance at each symbol
distances = []
for i,j in zip(tree,pair):
      start, end_word, end_len = find_start(j,i)
      seq = i[start:]
      distance = 0
      last = None
      k = 0
      left = 0
      right = 0
      while seq[k:k+end_len] != end_word:
            if seq[k] == ")":
                  if left != 0:
                        left = left -1
                        distance = distance -1
                  else:
                        right = right +1
                        if distance == right +2:
                              distance = distance -1
                        else:
                              distance = distance +1
            elif seq[k] == "," and distance == right and left ==0:
                   distance = distance +2
            elif seq[k] == "(":
                  distance = distance +1
                  left = left +1
            if seq[k] in ["(",")",","]:
                  last = seq[k]
            k = k+1
      distances.append(distance)
for i in distances:
      print i,
print

##Strategy 2: coung left/right parenthesis in between the 2 words
distances = []
for i,j in zip(tree,pair):
      start, end_word, end_len = find_start(j,i)
      seq = i[start:]
      left = 0
      right =0
      k = 0
      while seq[k:k+end_len] != end_word:
            if seq[k] == ")" and left:
                  left = left -1
            elif seq[k] == ")":
                  right = right +1
            elif seq[k] == "(":
                  left = left +1
            k = k+1
      if seq[k-1] == ")" and not left:
            distances.append(left + right)
      else:
            distances.append(left + right +2)
      
for i in distances:
      print i,
