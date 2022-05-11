from graph import Graph
import json

# nodes = ["Reykjavik", "Oslo", "Moscow", "London", "Rome", "Berlin", "Belgrade", "Athens"]
#
# edges = {}
# for node in nodes:
#     edges[node] = {}
#
# edges["Reykjavik"]["Oslo"] = 5
# edges["Reykjavik"]["London"] = 4
# edges["Oslo"]["Berlin"] = 1
# edges["Oslo"]["Moscow"] = 3
# edges["Moscow"]["Belgrade"] = 5
# edges["Moscow"]["Athens"] = 4
# edges["Athens"]["Belgrade"] = 1
# edges["Rome"]["Berlin"] = 2
# edges["Rome"]["Athens"] = 2


class MetroBuilder:
    def __init__(self):
        self.metro = Graph()

    def create_line(self, stations: list, value: int):
        """
        Получает список из стоящих по порядку станций метро и соединяет их ребрами с одинаковым весом.
        :return Словарь содержащий станции и тунелли между ними
        """
        edges = {}
        for station, next_station in zip(stations, stations[1:]):
            if next_station is not None:
                edges[station] = {f'{next_station}': value}
        self.metro.nodes.extend(stations)
        self.metro.edges.update(self.construct_graph(stations, edges))
        # return self.construct_graph(stations, edges)

    @staticmethod
    def construct_graph(nodes: list, edges: dict):
        """
        Этот метод обеспечивает симметричность графa. Для неориентированного графа
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

    def add_edge(self, station1: str, station2: str, value: int):
        self.metro.edges.update({station1: {station2: value}})

    def get_metro(self):
        return self.metro

    def save_metro(self, path: str):
        with open(path, 'w', encoding='utf8') as file:
            metro = {'nodes': self.metro.nodes,
                     'edges': self.metro.edges}
            json.dump(metro, file, indent=2, ensure_ascii=False)
