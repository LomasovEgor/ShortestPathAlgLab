class Graph(object):
    def __init__(self, nodes: list, edges: dict):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, edges)

    def construct_graph(self, nodes: list, edges):
        """
        Этот метод обеспечивает симметричность графика. Для неориентированного графа
        """
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(edges)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if not graph[adjacent_node].get(node, False):
                    graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        """
        Возвращает соседей узла
        """
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False):
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        """
        Возвращает значение ребра между двумя узлами.
        """
        return self.graph[node1][node2]
