from tkinter import ttk
import tkinter as tk
import json
from autocomplete_entrylistbox import *
from dijkstra_algorithm import dijkstra_algorithm
from graph import Graph


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Добавить начальный узел вручную
    path.append(start_node)
    time = "Марушут займет времени: {} мин.".format(shortest_path[target_node])
    path = "\n -> \n".join(reversed(path))
    return time, path


class StationEnterWin:
    def __init__(self, stations: list, graph):
        self.graph = graph
        self.stations = stations
        self.win = tk.Tk()
        self.win.tk.call("source", "Sun-Valley-ttk-theme-master/sun-valley.tcl")
        self.style = ttk.Style(self.win)
        self.win.tk.call("set_theme", "light")
        self.win.title('Метро')
        self.win.geometry('1150x850')

        self.picture = tk.Canvas(self.win, height=900, width=700)
        self.img = tk.PhotoImage(file='metro_img.png')
        self.metro_pic = self.picture.create_image(0, 0, anchor='nw', image=self.img)

        self.start_st_list = AutocompleteEntryListbox(self.win, width=30, completevalues=stations,
                                                      allow_other_values=True)
        self.end_st_list = AutocompleteEntryListbox(self.win, width=30, completevalues=stations,
                                                    allow_other_values=True)

        self.enter_btn = ttk.Button(self.win, text='Рассчитать маршрут', command=self.enter_btn_pressed)
        self.path_label = ttk.Label(self.win, text='Путь:')
        self.time_label = ttk.Label(self.win, text='Время:')

        self.place_widgets()

    def place_widgets(self):
        self.picture.grid(row=1, rowspan=10, column=1)
        self.start_st_list.grid(row=1, column=2)
        self.end_st_list.grid(row=2, column=2)
        self.enter_btn.grid(row=3, column=2)
        self.path_label.grid(row=1, column=3, rowspan=10)
        self.time_label.grid(row=5, column=2)

        self.win.mainloop()

    def enter_btn_pressed(self):
        start_station = self.start_st_list.get()
        end_station = self.end_st_list.get()
        previous_nodes, shortest_path = dijkstra_algorithm(graph=self.graph, start_node=start_station)
        time, path = print_result(previous_nodes, shortest_path, start_node=start_station, target_node=end_station)
        self.time_label.configure(text=time)
        self.path_label.configure(text=path)



def main():
    with open('testMetro.Json', 'r', encoding='utf-8') as file:
        metro = json.load(file)
    stations: list = metro['nodes']
    edges: dict = metro['edges']
    graph = Graph()
    graph.nodes = stations
    graph.edges = edges

    StationEnterWin(stations, graph)


if __name__ == '__main__':
    main()
