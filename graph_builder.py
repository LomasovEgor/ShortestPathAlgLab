from graph import Graph

nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]

edges = {}
for node in nodes:
    edges[node] = {}

edges["Reykjavik"]["Oslo"] = 5
edges["Reykjavik"]["London"] = 4
edges["Oslo"]["Berlin"] = 1
edges["Oslo"]["Moscow"] = 3
edges["Moscow"]["Belgrade"] = 5
edges["Moscow"]["Athens"] = 4
edges["Athens"]["Belgrade"] = 1
edges["Rome"]["Berlin"] = 2
edges["Rome"]["Athens"] = 2


def init_graph():
    return Graph(nodes, edges)
