import networkx as nx
import matplotlib.pyplot as plt
'''
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
'''

G = nx.empty_graph(8)
pos = nx.random_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos,
                       nodelist=[0, 1, 2, 3],
                       node_color='r',
                       node_size=500,
                       alpha=0.8)
nx.draw_networkx_nodes(G, pos,
                       nodelist=[4, 5, 6, 7],
                       node_color='b',
                       node_size=500,
                       alpha=0.8)

# edges
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
nx.draw_networkx_edges(G, pos,
                       edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
                       width=8, alpha=0.5, edge_color='r')
nx.draw_networkx_edges(G, pos,
                       edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
                       width=8, alpha=0.5, edge_color='b')


# some math labels
labels = {}
labels[0] = r'$a$'
labels[1] = r'$b$'
labels[2] = r'$c$'
labels[3] = r'$d$'
labels[4] = r'$\alpha$'
labels[5] = r'$\beta$'
labels[6] = r'$\gamma$'
labels[7] = r'$\delta$'
nx.draw_networkx_labels(G, pos, labels, font_size=16)

plt.axis('off')
plt.show()
