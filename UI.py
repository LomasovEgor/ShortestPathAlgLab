from tkinter import ttk
import tkinter as tk
import json
from autocomplete_entrylistbox import *


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Добавить начальный узел вручную
    path.append(start_node)

    print("Найден следующий лучший маршрут с ценностью {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


class StationEnterWin:
    def __init__(self, stations: list):
        self.stations = stations
        self.win = tk.Tk()
        self.win.tk.call("source", "Sun-Valley-ttk-theme-master/sun-valley.tcl")
        self.style = ttk.Style(self.win)
        self.win.tk.call("set_theme", "light")
        self.win.title('Метро')
        self.win.geometry('600x600')

        self.start_st_list = AutocompleteEntryListbox(self.win, width=30, completevalues=stations, allow_other_values=True)
        self.end_st_list = AutocompleteEntryListbox(self.win, width=30, completevalues=stations, allow_other_values=True)

        # self.end_st_entry = ttk.Entry(self.win, text='Начальная станция')

        # self.enter_btn = ttk.Button(self.win, text='Рассчитать маршрут')

        self.place_widgets()

    def place_widgets(self):

        self.start_st_list.pack()
        self.end_st_list.pack()
        # self.enter_btn.pack()
        self.win.mainloop()
    #
    # def enter_btn_pressed(self):
    #     pass

    def create_bindings(self):
        pass


def main():
    with open('testMetro.Json', 'r', encoding='utf-8') as file:
        metro = json.load(file)
    stations: list = metro['nodes']
    StationEnterWin(stations)


if __name__ == '__main__':
    main()
