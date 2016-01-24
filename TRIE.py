##Introduction to Pattern Matching
strings = ['ATAGA','ATC','GAT']
infile = open('rosalind_trie.txt','r')
strings = [i.rstrip('\n') for i in infile.readlines()]

class NODE():
      def __init__(self, label):
            self.label=label
            self.children = {}  #dictionary containing label:index

trie = [NODE('root')]
n = 1
for each_string in strings:
      parent = trie[0]
      for each_nucleo in each_string:
            if each_nucleo not in parent.children:
                  parent.children[each_nucleo] = n
                  trie.append(NODE(each_nucleo))
                  parent = trie[n]
                  n += 1
            else:
                  parent = trie[parent.children[each_nucleo]]

outfile = open('result.txt','w')
for i in range(len(trie)):
      children = trie[i].children
      for each_child in children:
            outfile.write(str(i+1)+' '+ str(children[each_child]+1) +' '+each_child+'\n')
outfile.close()

