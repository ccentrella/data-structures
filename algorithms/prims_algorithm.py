import json
import os
from os import path

class GraphEdge:
    def __init__(self, value, weight, next_edge=None):
        self.value: int = value
        self.weight: int = weight
        self.next_edge: GraphEdge = next_edge

class Graph:
    def __init__(self, file_location=None):
        self.edges: [GraphEdge] = []
        self.labels: [int] = []

        if file_location is not None:
            self.load_file(file_location)

    def load_file(self, file_location):
        with open(file_location, 'r') as file:
            data = file.read()
            graph_data = json.loads(data)
            graph_edges = graph_data['edges']
            graph_labels = graph_data['labels']
            graph_edge_weights = graph_data['edge-weights']

            for index, graph_edge in graph_edges.items():
                graph_label = graph_labels[index]
                graph_edge_weight = graph_edge_weights[index]
                self.add_vertex(graph_label, graph_edge, graph_edge_weight)

    def add_vertex(self, graph_label, edges=None, edge_weights=None):
        self.edges.append(None)
        self.labels.append(graph_label)

        if edges is not None:
            vertex = len(self.edges) - 1
            for index, edge in enumerate(edges):
                weight = edge_weights[index]
                self.add_edge(vertex, edge, weight)

    def add_edge(self, x, y, weight):
        current_edge = self.edges[x]
        new_edge = GraphEdge(y, weight, current_edge)
        self.edges[x] = new_edge

parent_directory = path.dirname(os.getcwd())
graph_file = path.join(parent_directory, 'data', 'graph.json')
graph = Graph(graph_file)
