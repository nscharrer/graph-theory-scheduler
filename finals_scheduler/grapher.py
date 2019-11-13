import networkx as nx
import matplotlib.pyplot as plt
import random

color_list = ['#48D1CC', '#00FFFF', '#8B0000', '#F5F5F5', '#FAEBD7', '#D2B48C', '#40E0D0', '#DCDCDC', '#D2691E', '#2E8B57', '#87CEFA', '#FFF8DC', '#00CED1', '#RRGGBB', '#8FBC8F', '#32CD32', '#006400', '#FAFAD2', '#DA70D6', '#AFEEEE', '#6A5ACD', '#00FA9A', '#DEB887', '#RRGGBB', '#FF1493', '#8B008B', '#FFFACD', '#708090', '#00FF7F', '#F08080', '#7FFF00', '#6B8E23', '#FFE4E1', '#FF4500', '#DDA0DD', '#FFFFFF', '#1E90FF', '#F4A460', '#RRGGBB', '#483D8B', '#008000', '#0000CD', '#RRGGBB', '#808000', '#7B68EE', '#A0522D', '#BC8F8F', '#FF69B4', '#FFEBCD', '#FF8C00', '#7FFFD4', '#800080', '#FFFAF0', '#FDF5E6', '#00FF00', '#DAA520', '#FFF0F5', '#228B22', '#E9967A', '#D8BFD8', '#FFD700', '#DB7093', '#008080', '#F5DEB3', '#BDB76B', '#RRGGBB', '#6495ED', '#800000', '#BA55D3', '#98FB98', '#C71585', '#7CFC00', '#87CEEB', '#66CDAA', '#000080', '#ADD8E6', '#00008B', '#FF00FF', '#ADFF2F', '#B0C4DE', '#CD853F', '#FFFF00', '#B22222', '#CD5C5C', '#F5F5DC', '#A9A9A9', '#00FFFF', '#2F4F4F', '#FFA500', '#FFE4B5', '#RRGGBB', '#FFDEAD', '#FA8072', '#RRGGBB', '#8B4513', '#FFEFD5', '#EEE8AA', '#F8F8FF', '#FF0000', '#4682B4', '#000000', '#778899', '#RRGGBB', '#90EE90', '#F5FFFA', '#FFC0CB', '#FF6347', '#FF00FF', '#FFA07A', '#E0FFFF', '#808080', '#008B8B', '#FF7F50', '#FFF5EE', '#F0E68C', '#EE82EE', '#F0F8FF', '#FFE4C4', '#0000FF', '#RRGGBB', '#696969', '#FAF0E6', '#00BFFF', '#9ACD32', '#F0FFF0', '#B0E0E6', '#9400D3', '#FFB6C1', '#C0C0C0', '#FFFFE0', '#9932CC', '#4B0082', '#3CB371', '#FFFAFA', '#E6E6FA', '#20B2AA', '#FFFFF0', '#RRGGBB', '#8A2BE2', '#5F9EA0', '#556B2F', '#4169E1', '#RRGGBB', '#191970', '#9370DB', '#D3D3D3', '#A52A2A', '#F0FFFF', '#FFDAB9', '#DC143C']

copy_color_list = ['#48D1CC', '#00FFFF', '#8B0000', '#F5F5F5', '#FAEBD7', '#D2B48C', '#40E0D0', '#DCDCDC', '#D2691E', '#2E8B57', '#87CEFA', '#FFF8DC', '#00CED1', '#RRGGBB', '#8FBC8F', '#32CD32', '#006400', '#FAFAD2', '#DA70D6', '#AFEEEE', '#6A5ACD', '#00FA9A', '#DEB887', '#RRGGBB', '#FF1493', '#8B008B', '#FFFACD', '#708090', '#00FF7F', '#F08080', '#7FFF00', '#6B8E23', '#FFE4E1', '#FF4500', '#DDA0DD', '#FFFFFF', '#1E90FF', '#F4A460', '#RRGGBB', '#483D8B', '#008000', '#0000CD', '#RRGGBB', '#808000', '#7B68EE', '#A0522D', '#BC8F8F', '#FF69B4', '#FFEBCD', '#FF8C00', '#7FFFD4', '#800080', '#FFFAF0', '#FDF5E6', '#00FF00', '#DAA520', '#FFF0F5', '#228B22', '#E9967A', '#D8BFD8', '#FFD700', '#DB7093', '#008080', '#F5DEB3', '#BDB76B', '#RRGGBB', '#6495ED', '#800000', '#BA55D3', '#98FB98', '#C71585', '#7CFC00', '#87CEEB', '#66CDAA', '#000080', '#ADD8E6', '#00008B', '#FF00FF', '#ADFF2F', '#B0C4DE', '#CD853F', '#FFFF00', '#B22222', '#CD5C5C', '#F5F5DC', '#A9A9A9', '#00FFFF', '#2F4F4F', '#FFA500', '#FFE4B5', '#RRGGBB', '#FFDEAD', '#FA8072', '#RRGGBB', '#8B4513', '#FFEFD5', '#EEE8AA', '#F8F8FF', '#FF0000', '#4682B4', '#000000', '#778899', '#RRGGBB', '#90EE90', '#F5FFFA', '#FFC0CB', '#FF6347', '#FF00FF', '#FFA07A', '#E0FFFF', '#808080', '#008B8B', '#FF7F50', '#FFF5EE', '#F0E68C', '#EE82EE', '#F0F8FF', '#FFE4C4', '#0000FF', '#RRGGBB', '#696969', '#FAF0E6', '#00BFFF', '#9ACD32', '#F0FFF0', '#B0E0E6', '#9400D3', '#FFB6C1', '#C0C0C0', '#FFFFE0', '#9932CC', '#4B0082', '#3CB371', '#FFFAFA', '#E6E6FA', '#20B2AA', '#FFFFF0', '#RRGGBB', '#8A2BE2', '#5F9EA0', '#556B2F', '#4169E1', '#RRGGBB', '#191970', '#9370DB', '#D3D3D3', '#A52A2A', '#F0FFFF', '#FFDAB9', '#DC143C']


def graph_tester0():
    G = nx.empty_graph(2)
    pos = nx.random_layout(G)  # positions for all nodes

    nx.draw_networkx_nodes(G, pos, nodelist=[0, 1], node_color=color_list.pop(), node_size=500)
    nx.draw(G, pos)
    plt.axis('off')

    plt.show()


def graph_tester1():
    G = nx.empty_graph(8)
    pos = nx.random_layout(G)  # positions for all nodes

    # nodes
    current_color = color_list.pop()
    nx.draw_networkx_nodes(G, pos,
                           nodelist=[0, 1, 2, 3],
                           node_color=current_color,
                           node_size=8000,
                           alpha=0.8)

    next_color = color_list.pop()
    nx.draw_networkx_nodes(G, pos,
                           nodelist=[4, 5, 6, 7],
                           node_color=next_color,
                           node_size=500,
                           alpha=0.8)

    color_list.append(current_color)
    color_list.append(next_color)

    # edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edges(G, pos,
                           edgelist=[(0, 1), (1, 2), (2, 3), (3, 0)],
                           width=8, alpha=0.5, edge_color=color_list.pop())
    nx.draw_networkx_edges(G, pos,
                           edgelist=[(4, 5), (5, 6), (6, 7), (7, 4)],
                           width=8, alpha=0.5, edge_color=color_list.pop())


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


def graph_courses(conflict_dict):
    num_courses = len(conflict_dict)
    graph = nx.empty_graph(num_courses)
    pos = nx.spring_layout(graph)  # positions for all nodes
    node_num = 0
    labels = {}
    node_colors = []
    node_num_dict = {}
    node_list = []
    edge_list = []

    for course in conflict_dict:
        node_num_dict[course] = node_num
        node_num += 1

    for course in conflict_dict:
        conflicts, color = conflict_dict[course]

        current_node_num = node_num_dict[course]
        node_list.append(current_node_num)
        node_colors.append(color)
        labels[current_node_num] = course

        for conflict in conflicts:
            edge_list.append((current_node_num, node_num_dict[conflict]))

    nx.draw_networkx_nodes(graph, pos,
                           nodelist=node_list,
                           node_color=node_colors,
                           node_size=500,
                           alpha=0.8)
    nx.draw_networkx_edges(graph, pos,
                           edgelist=edge_list,
                           width=2, alpha=0.5, edge_color='#000000')

    nx.draw_networkx_labels(graph, pos, labels, font_size=8)
    plt.axis('off')
    plt.show()


def greedy_coloring(conflict_dict):
    if len(conflict_dict) == 0:
        # todo raise error
        print("Conflict dict empty")
        return -1
    all_keys = list(conflict_dict)
    first_color = color_list.pop()
    conflicts, color = conflict_dict[all_keys[0]]
    color = first_color
    conflict_dict[all_keys[0]] = (conflicts, color)

    color_list.append(color)

    for i in range(1, len(all_keys)):
        conflicts, color = conflict_dict[all_keys[i]]
        used_colors = []
        # go through all conflicting courses (edges) to see what colors are used
        for course in conflicts:
            temp_conflicts, course_color = conflict_dict[course]
            if course_color is not None:
                used_colors.append(course_color)
                color_list.remove(course_color)

        color = color_list.pop()
        conflict_dict[all_keys[i]] = (conflicts, color)

        color_list.append(color)
        for used_color in used_colors:
            color_list.append(used_color)

    return conflict_dict


