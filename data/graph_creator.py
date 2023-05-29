import json
import os
import random
from os import path

def create_vertices(graph_edges, maximum=2000):
    for index, graph_edge in graph_edges.items():
        length = len(graph_edge)
        weights = []
        for i in range(length):
            random_int = random.randint(0, maximum)
            weights.append(random_int)
        print(f'\"{index}\": {weights},')

def open_file(file_location):
    with open(file_location, 'r') as file:
        data = file.read()
        graph_data = json.loads(data)
        return graph_data['edges']

parent_directory = os.getcwd()
graph_file = path.join(parent_directory, 'graph-extended.json')
graph_edges = open_file(graph_file)
create_vertices(graph_edges, 200)
