import community
import networkx as nx
from matplotlib import pyplot as plt
from sklearn import metrics
from pyitlib import discrete_random_variable as drv
import collections
import sys
from sklearn.metrics import normalized_mutual_info_score

nn=int(sys.argv[1])
p=float(sys.argv[2].replace(",", "."))

G=nx.read_edgelist("rewired.dat")
#pos = nx.spring_layout(G)
#nx.draw_networkx(G,pos,node_size=5,alpha=0.5,with_labels=False)
#plt.show()

partition = community.best_partition(G)
#print partition

part = collections.OrderedDict(sorted(partition.items(), key=lambda x: int(x[0])))

rever = part
#print rever

lista = [ v for v in rever.values() ]
#print lista

communes = []

for i in range(16):
   for j in range(40):
      communes.append(i)

#print communes 
c = drv.entropy(lista)
eta = drv.information_mutual(lista, communes)
eta = eta/c
print p, eta

#nmi = normalized_mutual_info_score(lista,communes,average_method='arithmetic')
#print p,nmi
