import json
from graph import Graph
from UI import StationEnterWin


def main():
    with open('testMetro.Json', 'r', encoding='utf-8') as file:
        metro = json.load(file)
    stations: list = metro['nodes']
    edges: dict = metro['edges']
    graph = Graph()
    graph.nodes = stations
    graph.edges = edges
    StationEnterWin(stations, graph)


if __name__ == 'main':
    main()
