from igraph import *
from sklearn import metrics
import sys

p=float(sys.argv[1].replace(",", "."))

# load data into a graph
#p=0.01
g1 = Graph.Read_Ncol('edge.dat', directed = False)
g1.rewire_edges(p, loops=False, multiple=False)

g1.write_edgelist('rewired.dat')
#plot(g1)  

