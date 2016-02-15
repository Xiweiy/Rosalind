##Using the Spectrum Graph to infer peptide
##http://rosalind.info/problems/sgra/

##Note: algm almost inherit from FULL.py (Inferring Peptide from Full Spectrum)


Mass = [57.02146,71.03711,87.03203,97.05276,99.06841,101.04768,103.00919,
        113.08406,114.04293,115.02694,128.05858,128.09496,129.04259,131.04049,
        137.05891,147.06841,156.10111,163.06333,186.07931]
AA = ['G','A','S','P','V','T','C','I','N','D','Q','K','E','M','H','F','R','Y','W']

infile = open('rosalind_sgra.txt','r')
Spec = [float(i.rstrip('\n')) for i in infile.readlines()]
#Spec = [3524.8542,3623.5245,3710.9335,3841.974,3929.00603,3970.0326,4026.05879,4057.0646,4083.08025]


##Could use binary search for optimization, but may not be necessary for a list of 20 element
def find_closest(each_peak):
      index = 0
      mindiff = 1000
      curdiff = abs(each_peak - Mass[index])
      while curdiff < mindiff:
            index += 1
            mindiff = curdiff
            if index > 18:
                  return index-1, mindiff
            else:
                  curdiff = abs(each_peak - Mass[index])      
      return index-1, mindiff

Spec = sorted(Spec)

class Node:
      def __init__(self, peak):
            self.peak = peak
            self.parent = None
            self.forward = []

class Edge:
      def __init__(self, parent, child, aa):
            self.parent = parent
            self.child = child
            self.aa = aa


##Step 1: Find Neighbors
n = len(Spec)
nodes = [Node(Spec[i]) for i in range(n)]
for i in range(n):
      for j in range(i+1,n):
            diff = nodes[j].peak - nodes[i].peak 
            if diff > 187:
                  break
            else:
                  index, mindiff = find_closest(diff)
                  if mindiff < 0.05:
                        nodes[i].forward.append(Edge(nodes[i],nodes[j], AA[index]))
                        ##not assign any value to the parent attribute because parent is unknown now

##Step 2: DFS
maxlength = 0
for i in nodes:
      #b = {round(i.peak,5): round(parent - i.peak,5)}     ##peaks already in the chain
      t = ''       #ongoing chain's sequence
      chain = []   #the list of current branch
      unvisited_edges = []    #the list of branching point of the tree
      cur_node = i

      ##the parent of current node's children is the current node
      for m in cur_node.forward:
           m.parent = cur_node    

      #stop if there is no further child on the current branch, and no other potential braches
      while len(cur_node.forward) or len(unvisited_edges):
            
            ##if there is still child on this branch, extend the ongoing chains (b, t, chain, (unvisited lists))
            if len(cur_node.forward):
                  t += cur_node.forward[0].aa
                  cur_node = cur_node.forward[0].child
                  chain.append(cur_node)
                  if len(cur_node.forward) > 1:
                        unvisited_edges += cur_node.forward[1:]

            ##if there is no further child on this branch, traceback to find other branching point
                        ##delete the nodes on the ongonig chains after the new branching point
            else:
                  if len(t) > maxlength:
                        maxlength = len(t)
                        T = t
                  traceback = unvisited_edges[-1].parent
                  while chain[-1].peak != traceback.peak:
                        chain.pop(-1)
                        t = t[:-1]
                        if not len(chain):
                              if len(t) > maxlength:
                                    maxlength = len(t)
                                    T= t
                              break
                  cur_node = unvisited_edges[-1].child
                  t += unvisited_edges[-1].aa
                  unvisited_edges.pop(-1)
                  chain.append(cur_node)
      if len(t) > maxlength:
            maxlength = len(t)
            T= t
print T

