import networkx as nx
import matplotlib.pyplot as plt

color_list = ['#48D1CC', '#00FFFF', '#8B0000', '#F5F5F5', '#FAEBD7', '#D2B48C', '#40E0D0', '#DCDCDC', '#D2691E',
              '#2E8B57', '#87CEFA', '#FFF8DC', '#00CED1', '#RRGGBB', '#8FBC8F', '#32CD32', '#006400', '#FAFAD2',
              '#DA70D6', '#AFEEEE', '#6A5ACD', '#00FA9A', '#DEB887', '#RRGGBB', '#FF1493', '#8B008B', '#FFFACD',
              '#708090', '#00FF7F', '#F08080', '#7FFF00', '#6B8E23', '#FFE4E1', '#FF4500', '#DDA0DD', '#FFFFFF',
              '#1E90FF', '#F4A460', '#RRGGBB', '#483D8B', '#008000', '#0000CD', '#RRGGBB', '#808000', '#7B68EE',
              '#A0522D', '#BC8F8F', '#FF69B4', '#FFEBCD', '#FF8C00', '#7FFFD4', '#800080', '#FFFAF0', '#FDF5E6',
              '#00FF00', '#DAA520', '#FFF0F5', '#228B22', '#E9967A', '#D8BFD8', '#FFD700', '#DB7093', '#008080',
              '#F5DEB3', '#BDB76B', '#RRGGBB', '#6495ED', '#800000', '#BA55D3', '#98FB98', '#C71585', '#7CFC00',
              '#87CEEB', '#66CDAA', '#000080', '#ADD8E6', '#00008B', '#FF00FF', '#ADFF2F', '#B0C4DE', '#CD853F',
              '#FFFF00', '#B22222', '#CD5C5C', '#F5F5DC', '#A9A9A9', '#00FFFF', '#2F4F4F', '#FFA500', '#FFE4B5',
              '#RRGGBB', '#FFDEAD', '#FA8072', '#RRGGBB', '#8B4513', '#FFEFD5', '#EEE8AA', '#F8F8FF', '#FF0000',
              '#4682B4', '#000000', '#778899', '#RRGGBB', '#90EE90', '#F5FFFA', '#FFC0CB', '#FF6347', '#FF00FF',
              '#FFA07A', '#E0FFFF', '#808080', '#008B8B', '#FF7F50', '#FFF5EE', '#F0E68C', '#EE82EE', '#F0F8FF',
              '#FFE4C4', '#0000FF', '#RRGGBB', '#696969', '#FAF0E6', '#00BFFF', '#9ACD32', '#F0FFF0', '#B0E0E6',
              '#9400D3', '#FFB6C1', '#C0C0C0', '#FFFFE0', '#9932CC', '#4B0082', '#3CB371', '#FFFAFA', '#E6E6FA',
              '#20B2AA', '#FFFFF0', '#RRGGBB', '#8A2BE2', '#5F9EA0', '#556B2F', '#4169E1', '#RRGGBB', '#191970',
              '#9370DB', '#D3D3D3', '#A52A2A', '#F0FFFF', '#FFDAB9', '#DC143C']


def greedy_coloring(conflict_dict):
    """
    Uses the Greedy algorithm to color all vertices
    :param conflict_dict: Dictionary containing each course and the courses that conflict with it
    :return: Same dictionary as was passed in but each course also maps to a color as well
    """
    # Check if the data passed in has anything
    if len(conflict_dict) == 0:
        print("Conflict dict empty")
        return -1

    all_keys = list(conflict_dict)

    # Assign the first class the first color in the list
    first_color = color_list.pop()
    conflicts, color = conflict_dict[all_keys[0]]
    color = first_color
    conflict_dict[all_keys[0]] = (conflicts, color)

    # put the color back
    color_list.append(color)

    # Second part of Greedy algorithm
    for i in range(1, len(all_keys)):
        conflicts, color = conflict_dict[all_keys[i]]
        used_colors = []

        # go through all conflicting courses (adjacent vertices) to see what colors are used
        for course in conflicts:
            temp_conflicts, course_color = conflict_dict[course]
            if course_color is not None:
                used_colors.append(course_color)
                color_list.remove(course_color)

        # get the next available color and assign it to this vertex
        color = color_list.pop()
        conflict_dict[all_keys[i]] = (conflicts, color)

        # put that color back, and then put back the other used colors
        color_list.append(color)
        for used_color in used_colors:
            color_list.append(used_color)

    return conflict_dict


def graph_courses(conflict_dict):
    """
    Take the colored conflict dictionary and create a plot of all courses and conflicts
    :param conflict_dict: dictionary with courses as keys and their conflict and color as mappings
    :return: True if graphing goes correctly
    """
    # initialize the graph - spring layout makes all nodes as far apart as possible for visual ease
    num_courses = len(conflict_dict)
    graph = nx.empty_graph(num_courses)
    pos = nx.spring_layout(graph)  # positions for all nodes

    node_num = 0
    labels = {}
    node_colors = []
    node_num_dict = {}
    node_list = []
    edge_list = []

    # map each course to a node number
    for course in conflict_dict:
        node_num_dict[course] = node_num
        node_num += 1

    # get each course out of the dictionary along with its color and set a label for it
    # also add it's edges based on the conflicting courses
    for course in conflict_dict:
        conflicts, color = conflict_dict[course]

        current_node_num = node_num_dict[course]
        node_list.append(current_node_num)
        node_colors.append(color)
        labels[current_node_num] = course

        # the current node conflicts with all nodes in its conflict list, so we need to add that to the edges
        for conflict in conflicts:
            edge_list.append((current_node_num, node_num_dict[conflict]))

    # draw the nodes, edges, and labels and show the plot
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
