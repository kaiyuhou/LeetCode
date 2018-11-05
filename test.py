import networkx as nx
import matplotlib.pyplot as plt
# import numpy as np

Matrix = [
        [0, 1, 1, 1, 1, 1, 0, 0],  # a
        [0, 0, 1, 0, 1, 0, 0, 0],  # b
        [0, 0, 0, 1, 0, 0, 0, 0],  # c
        [0, 0, 0, 0, 1, 0, 0, 0],  # d
        [0, 0, 0, 0, 0, 1, 0, 0],  # e
        [0, 0, 1, 0, 0, 0, 1, 1],  # f
        [0, 0, 0, 0, 0, 1, 0, 1],  # g
        [0, 0, 0, 0, 0, 1, 1, 0]  # h
        ]

G = nx.Graph()


for i in range(len(Matrix)):
    for j in range(len(Matrix)):
        if Matrix[i][j] == 1:
            G.add_edge(i, j)

node_labels = {node: name for (node, name) in zip(G.nodes(), ["a", "b", "c", "d", "e", "f", "g", "h"])}
node_color = [1, 2, 3, 1, 2, 3, 1, 2]

edge_color = []
edge_labels = {}
for index, edge in enumerate(G.edges()):
    if index % 2 == 0:
        edge_color.append('k')
        edge_labels[edge] = "label"
    else:
        edge_color.append('r')

# position = nx.circular_layout(G)
position = nx.spring_layout(G)

nx.draw_networkx_nodes(G, position, node_size=500, node_color=node_color)  #with_labels=True
nx.draw_networkx_labels(G, position, labels=node_labels)

nx.draw_networkx_edges(G, position, edge_color=edge_color)
nx.draw_networkx_edge_labels(G, position, edge_labels=edge_labels)

plt.axis('off')
plt.show()
plt.savefig('routing.png')