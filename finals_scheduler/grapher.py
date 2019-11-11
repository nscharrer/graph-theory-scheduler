import networkx as nx
import matplotlib.pyplot as plt

e = [(1, 2), (2, 3), (3, 1)]  # list of edges
d = {0: {1: 1}}  # dict-of-dicts single edge (0,1)

G = nx.Graph()

G.add_nodes_from(nodes_for_adding=[0,1,2,3], node_color='red')
G.add_edges_from(ebunch_to_add=[(0,1),(1,2),(2,3),(3,0)])


pos = nx.random_layout(G)
#nx.draw_networkx_nodes(G, pos, nodelist=[0,1,2,3], node_color='r')

#nx.draw_networkx(G, pos, nodelist=[0,1,2,3], node_color='r', edgelist=[(0,1),(1,2),(2,3),(3,0)], node_size=500, alpha=0.8, width=8)

nx.draw(G, pos)

plt.show()
