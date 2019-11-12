import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

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


'''
G = nx.empty_graph(8)
pos = nx.random_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos,
                       nodelist=[0, 1, 2, 3],
                       node_color='r',
                       node_size=8000,
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
labels[0] = r'$CE\ 4000\ 001$'
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
'''


def graph_courses(conflict_dict):
    num_courses = len(conflict_dict)
    graph = nx.empty_graph(num_courses)
    pos = nx.random_layout(graph)  # positions for all nodes
    node_num = 0
    labels = {}
    cmap = cm.get_cmap('Pastel1')

    for course in conflict_dict:
        conflicts = conflict_dict[course]
        adj_courses = conflicts
        #adj_courses.append(conflicts)
        adj_courses.append(course)
        node_list = []
        edge_list = []

        node_color = cmap(random.random())

        for i in range(len(adj_courses)):
            node_list.append(node_num)
            labels[node_num] = adj_courses[i]
            for j in range(i+1, len(adj_courses)):
                edge_list.append((node_num, node_num+j))

        #todo the colors need to be different for the adjacent nodes - need to fix that 
        nx.draw_networkx_nodes(graph, pos,
                               nodelist=node_list,
                               node_color=node_color,
                               node_size=500,
                               alpha=0.8)
        nx.draw_networkx_edges(graph, pos,
                               edgelist=edge_list,
                               width=8, alpha=0.5, edge_color='b')

        node_num += 1

    nx.draw_networkx_labels(graph, pos, labels, font_size=16)
    plt.axis('off')
    plt.show()
