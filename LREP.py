##Finding the Longest Multiple Repeat
##http://rosalind.info/problems/lrep/

infile = open('rosalind_lrep.txt','r')
inlist = infile.readlines()
infile.close()

S = inlist[0].rstrip('\n')
k = int(inlist[1].rstrip('\n'))

class NODE:
      def __init__(self):
            self.forward = []
            self.reverse = 0
            self.nchild = 0
            self.visited = 0

      def find_nchild(self):
            if not len(self.forward):
                  return 0
            children = self.forward
            total_children = 0
            for i in children:
                  cur_child = i.child
                  if not cur_child.visited:
                        cur_child.nchild = cur_child.find_nchild()
                        cur_child.visited = 1
                  if cur_child.nchild:
                        total_children += cur_child.nchild
                  else:
                        total_children += 1                     
            return total_children

      def find_motif(self):
            cur_node = self
            motif = ''
            while cur_node.reverse !=0:
                  start, length = cur_node.reverse.span
                  motif = S[start:start+length]+motif
                  cur_node = cur_node.reverse.parent
            return motif
            

class EDGE:
      def __init__(self, parent, child, start, length):
            self.parent = parent
            self.child = child
            self.span = [start-1, length]

            
maxnode = 0
nodes = []
for line in inlist[2:]:
      edge = line.rstrip('\n').split(' ')
      node1, node2 = int(edge[0][4:]), int(edge[1][4:])
      start, length = int(edge[2]), int(edge[3])
      if node2 > maxnode:
            nodes += [NODE() for i in range(node2-maxnode)]   ##cannot use NODE()*Constant since objects are passed by reference
            maxnode = node2
      cur_edge = EDGE(nodes[node1-1], nodes[node2-1], start, length)
      nodes[node1-1].forward.append(cur_edge)
      nodes[node2-1].reverse = cur_edge

index = 0                        
for i in nodes:
      index +=1
      if not i.visited:
            i.nchild = i.find_nchild()


maxmotif = ''
maxlength = 0
for i in nodes:
      if i.nchild >= k:
            motif = i.find_motif()
            if len(motif) > maxlength:
                  maxlength = len(motif)
                  maxmotif = motif
print maxmotif
