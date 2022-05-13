import json
from pyvis.network import Network

network = Network('1000px', '1000px', notebook=True, )

with open('testMetro.Json', 'r', encoding='utf-8') as file:
    metro = json.load(file)

labels: list = metro['nodes']
edges: dict = metro['edges']

id_dic = {}
for count, node in enumerate(labels):
    id_dic[node] = count + 1


def fill_nodes(id_dic: dict):
    nodes = []
    for value in id_dic.values():
        nodes.append(value)
    return nodes


def fill_labels_titles(id_dic: dict):
    labels = []
    for key in id_dic.keys():
        labels.append(key)
    return labels, labels


nodes = fill_nodes(id_dic)
labels, titles = fill_labels_titles(id_dic)

network.add_nodes(nodes=nodes, label=labels, title=titles)

network_edges = []

for key, edge_dict in edges.items():
    start_node_i = id_dic[key]
    for end_key, value in edge_dict.items():
        end_node_i = id_dic[end_key]
        network_edges.append((start_node_i, end_node_i, value))

network.add_edges(network_edges)

network.show_buttons(filter_=True)
network.show('test_network.html')
