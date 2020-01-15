import community
import networkx as nx
from matplotlib import pyplot as plt
from sklearn import metrics
from pyitlib import discrete_random_variable as drv
import sys

n1=int(sys.argv[1])
n2=int(sys.argv[2])
n3=int(sys.argv[3])
n4=int(sys.argv[4])

G1 = nx.complete_graph(n1)
G2 = nx.complete_graph(n2)
G3 = nx.complete_graph(n3)
G4 = nx.complete_graph(n4)

U1 = nx.disjoint_union(G1, G2)
U2 = nx.disjoint_union(G3, G4)

G = nx.disjoint_union(U1, U2)
#print G4.nodes
nx.write_edgelist(G,"edge.dat")
