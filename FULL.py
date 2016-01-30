##Inferring Peptide from Full Spectrum

Mass = [57.02146,71.03711,87.03203,97.05276,99.06841,101.04768,103.00919,
        113.08406,114.04293,115.02694,128.05858,128.09496,129.04259,131.04049,
        137.05891,147.06841,156.10111,163.06333,186.07931]
AA = ['G','A','S','P','V','T','C','I','N','D','Q','K','E','M','H','F','R','Y','W']

inputfile = open('rosalind_full.txt','r')
Spec = [float(i.rstrip('\n')) for i in inputfile.readlines()]
'''
Spec = [1988.21104821, 610.391039105, 738.485999105, 766.492149105, 863.544909105,
867.528589105,992.587499105,995.623549105,1120.6824591,1124.6661391,1221.7188991,
1249.7250491,1377.8200091]
'''
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


parent = Spec[0]
Spec = sorted(Spec[1:])


###############################################################################
####Method 1: Flawed Algm: Since only consider the first possible peak##########
################################################################################

'''
b = {round(Spec[0],5):round(parent-Spec[0],5)}
prev_spec = Spec[0]
t = ''
for i in Spec:
      complement = parent - i
      if round(i,5) not in b and round(complement,5) not in b:
            diff = i - prev_spec
            index, mindiff = find_closest(diff)
            #print mindiff
            if mindiff < 0.5:
                  t += AA[index]
                  b[round(i,5)] = round(complement,5)
                  prev_spec = i
print t
'''

##############################################################################      
###Method 2: First find all larger neighbor of each peak, then use DFS########
##############################################################################

class Node:
      def __init__(self, peak):
            self.peak = peak
            self.parent = None
            self.children = []
            self.childaa = []


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
                        nodes[i].children.append(nodes[j])
                        nodes[i].childaa.append(AA[index])


##Step 2: DFS
maxlength = 0
for i in nodes:
      b = {round(i.peak,5): round(parent - i.peak,5)}     ##peaks already in the chain
      t = ''       #ongoing chain's sequence
      chain = []   #the list of current branch
      unvisited_child = []    #the list of branching point of the tree
      unvisited_aa = []       #labels of unvisited_child[]
      cur_node = i

      ##CHILD is un-explored version of cur_node.children, containing all element not in b
      CHILD = cur_node.children   
      CHILDAA = cur_node.childaa

      ##the parent of current node's children is the current node
      for m in CHILD:
           m.parent = cur_node    

      #stop of their is no further child on the current branch, and no other potential braches
      while len(CHILD) or len(unvisited_child):
            
            ##if there is still child on this branch, extend the ongoing chains (b, t, chain, (unvisited lists))
            if len(CHILD):        
                  cur_node = CHILD[0]
                  b[round(cur_node.peak,5)] = round(parent - cur_node.peak,5)
                  t += CHILDAA[0]
                  chain.append(cur_node)
                  if len(CHILD) > 1:
                        unvisited_child += CHILD[1:]
                        unvisited_aa += CHILDAA[1:]

            ##if there is no further child on this branch, traceback to find other branching point
                        ##delete the nodes on the ongonig chains after the new branching point
            else:
                  traceback = unvisited_child[-1].parent
                  while chain[-1].peak != traceback.peak:
                        last_peak = round(chain[-1].peak,5)
                        last_complement = round(parent - last_peak,5)
                        if last_peak in b:
                              del b[last_peak]
                        if last_complement in b:
                              del b[last_complement]
                        chain.pop(-1)
                        t = t[:-1]
                        if not len(chain):
                              break
                  cur_node = unvisited_child[-1]
                  t += unvisited_aa[-1]
                  unvisited_child.pop(-1)
                  b[round(cur_node.peak,5)] = round(parent - cur_node.peak,5)
                  chain.append(cur_node)

            ##Generate the new CHILD list for the new node on the ongoing chain
            if len(cur_node.children):
                  CHILD = []
                  CHILDAA =[]
                  for m in range(len(cur_node.children)):
                        each_peak = cur_node.children[m].peak
                        complement = parent - each_peak
                        if round(each_peak,5) not in b and round(complement,5) not in b:
                              cur_node.children[m].parent = cur_node
                              CHILD.append(cur_node.children[m])
                              CHILDAA.append(cur_node.childaa[m])
            elif len(t) ==n/2-1:
                  print t
                  break
            else:
                  CHILD = []
            if len(t) > maxlength:
                  maxlength = len(t)

