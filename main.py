from pyvis.network import Network
from network_data import NetworkData

network = Network('600px', '600px', notebook=True, )


data = NetworkData()

nodes = []
labels = []
titles = []
colors = []

for values in data.test_data.values():
    nodes.append(values['node'])
    labels.append(values['label'])
    titles.append(values['title'])
    colors.append(values['color'])

network.add_nodes(nodes=nodes, label=labels, title=titles, color=colors)

print(nodes)
print(labels)
print(titles)
print(colors)

#
# network.add_edges([(1, 2, 10), (2, 3, 5), (3, 4, 5), (3, 5, 2), (2, 6, 2), (6, 7, 2),
#                    (6, 8, 2), (6, 9, 2), (6, 10, 2)])

network.show('test_network.html')
