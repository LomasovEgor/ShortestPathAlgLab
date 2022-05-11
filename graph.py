class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        """
        Возвращает соседей узла
        """
        connections = []
        for out_node in self.nodes:
            if self.edges[node].get(out_node, False):
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        """
        Возвращает значение ребра между двумя узлами.
        """
        return self.edges[node1][node2]
