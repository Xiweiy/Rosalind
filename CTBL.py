##Creating a Character Table

infile = open('rosalind_ctbl.txt','r')
newick = infile.readlines()[0][1:]   ##remove the leftmost open parenthesis
#newick = 'dog,((elephant,mouse),robot),cat);'


class Node:
      def __init__(self, attribute, parent):
            self.attribute = attribute  #root/internal/leaf
            self.child = []
            self.parent = parent


nodes = [Node('root', None)]
cur_parent = nodes[0]
index = 0   #count number of node in the tree
string = ''
taxa = []
for i in newick:
      #print i
      if i == '(':
            new_node = Node('internal', cur_parent)
            cur_parent.child.append(new_node)
            cur_parent = new_node
            nodes.append(cur_parent)
            index += 1
      elif i == ')' or i == ',':
            if len(string):
                  new_node = Node(string, cur_parent)
                  cur_parent.child.append(new_node)
                  nodes.append(new_node)
                  taxa.append(string)
                  string = ''
                  index += 1
            if i ==')':
                  cur_parent = cur_parent.parent
      else:
            string += i


def find_all_child(node):
      curnode = node
      children = [curnode]
      leaves = []
      while len(children):
            #print children
            children.pop(0)
            if curnode.attribute != 'internal':
                  leaves.append(curnode.attribute)
            children += curnode.child
            if len(children):
                  curnode = children[0]
      return leaves


'''
###########Method 1: Use Pandas DataFrame to Construct the Matrix########
from pandas import DataFrame
matrix = DataFrame(columns = sorted(taxa), dtype = int)
ntaxa = len(taxa)
row = 0
for i in nodes:
      if i.attribute == 'internal':
            leaves = find_all_child(i)
            if len(leaves):
                  row += 1
                  matrix.loc[row] = [0]*ntaxa
                  matrix.loc[row, leaves] = 1
print matrix
'''


#########Method 2: standard Python ###################
column_pos = {}
pos = 0
for i in sorted(taxa):
      column_pos[i] = pos
      pos += 1

ntaxa = pos
row = 0
outfile = open('result.txt','w')
for i in nodes[1:]:
      leaves = find_all_child(i)
      #print leaves
      if len(leaves) > 1:
            binary_string = '0'*ntaxa
            for each_leaf in leaves:
                  change_pos = column_pos[each_leaf]
                  binary_string = binary_string[:change_pos]+'1'+binary_string[change_pos+1:]
            outfile.write( binary_string +'\n')
outfile.close()
                
