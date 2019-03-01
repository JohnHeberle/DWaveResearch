# Basic program run on a quantum computer as outlined in 
# https://www.youtube.com/watch?v=ckJ59gsFllU. The program
# takes multiple antenas and maximizes the amount of antenas 
# with no antenas overlapping.

import networkx as nx
import dwave_networkx as dnx
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler(profile='quallect'))

G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (2,3), (3,4), (3,5), (4,5), (4,6), (5,6), (6,7)])

S = dnx.maximum_independent_set(G, sampler=sampler, num_reads=10)

print('Maximum independent set size found is', len(S))
print(S)

k = G.subgraph(S)
notS = list(set(G.nodes())-set(S))
othersubgraph = G.subgraph(notS)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G, pos=pos)
nx.draw(k, pos=pos)
nx.draw(othersubgraph, pos=pos, node_color='b')
plt.show()