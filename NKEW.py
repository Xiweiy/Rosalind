##Newick Format with Edge Weights
##http://rosalind.info/problems/nkew/

class NODE:
      def __init__(self, attribute):
            self.attribute = attribute  #root/internal/leaf
            self.forward = []
            self.backward = 0

      def path_root(self):
            cur_node = self
            distance = 0
            path_distance = {cur_node.attribute:distance}
            while cur_node.backward:
                  distance += cur_node.backward.length
                  cur_node = cur_node.backward.parent
                  path_distance[cur_node.attribute] = distance
            return path_distance

class EDGE:
      def __init__(self, parent, child):
            self.parent = parent
            self.child = child
            self.length = 0

def parse_newick(newick, species1, species2):
      nodes = [NODE('root')]
      cur_parent = nodes[0]
      string = ''
      taxa = {species1:0, species2:0}
      index = 0   #keep track of position of taxa
      for i in newick:
            if i == '(':
                  new_node = NODE('internal'+str(index))
                  new_edge = EDGE(cur_parent, new_node)
                  cur_parent.forward.append(new_edge)
                  new_node.backward = new_edge
                  cur_parent = new_node
                  nodes.append(cur_parent)
                  index +=1
            elif i == ':':  
                  if len(string):
                        new_node = NODE(string)
                        new_edge = EDGE(cur_parent, new_node)
                        new_node.backward = new_edge
                        cur_parent.forward.append(new_node.backward)
                        nodes.append(new_node)
                        index += 1
                        if string in taxa:
                              taxa[string] = index
                        string = '' 
            elif i == ')' or i == ',':
                  if not new_edge.length:
                        new_edge.length = int(string)
                        string = ''
                  else:
                        cur_parent.forward[-1].length = int(string)
                        string = ''
                  if i ==')':
                        cur_parent = cur_parent.backward.parent
            else:
                  string += i
      path1 = nodes[taxa[species1]].path_root()
      path2 = nodes[taxa[species2]].path_root()
      commonpath = []
      for i in path2:
            if i in path1:
                  commonpath.append( path2[i] + path1[i])
      print min(commonpath),


infile = open('rosalind_nkew.txt','r')
inlist = infile.readlines()

i = 0
for each_line in inlist:
      if not i%3:
            newick = inlist[i].rstrip(';\n')
            species1, species2 = inlist[i+1].rstrip('\n').split(' ')
            parse_newick(newick, species1, species2)
      i += 1


