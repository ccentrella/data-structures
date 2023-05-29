import json
import os
import random
from os import path

class GraphCreator:
    def __init__(self, file_location=None):
        self.graph_edges = {}
        self.graph_edge_weights = {}

        if file_location is not None:
            self.open_file(file_location)

    def open_file(self, file_location):
        with open(file_location, 'r') as file:
            data = file.read()
            graph_data = json.loads(data)
            self.graph_edges = graph_data['edges']
            if 'edge-weights' in graph_data:
                self.graph_edge_weights = graph_data['edge-weights']

    def create_vertices(self, vertex_count, maximum_edges=20, maximum_weight=2000):
        self.create_edges(vertex_count, maximum_edges)
        self.create_weights(maximum_weight)

    def create_edges(self, vertex_count, maximum_edges):
        self.begin_processing_edges()
        self.graph_edges = {}
        for index in range(vertex_count):
            edges = []
            edge_count = random.randint(0, maximum_edges)
            for edge_index in range(edge_count):
                random_vertex = random.randint(0, vertex_count - 1)
                edges.append(random_vertex)
            print(f'\"{index}\": {edges},')
            self.graph_edges[index] = edges
        self.finish_processing_edges()

    def create_weights(self, maximum_weight=2000):
        self.begin_processing_weights()
        self.graph_edge_weights = {}
        for index, graph_edge in self.graph_edges.items():
            length = len(graph_edge)
            weights = []
            for i in range(length):
                random_int = random.randint(0, maximum_weight)
                weights.append(random_int)
            print(f'\"{index}\": {weights},')
            self.graph_edge_weights[index] = weights
        self.finish_processing_weights()

    @staticmethod
    def begin_processing_edges():
        print("Creating edges...\n")

    @staticmethod
    def finish_processing_edges():
        print("\nEdges created successfully.\n")

    @staticmethod
    def begin_processing_weights():
        print("Creating weights...\n")

    @staticmethod
    def finish_processing_weights():
        print("\nWeights created successfully.\n")

parent_directory = os.getcwd()
graph_file = path.join(parent_directory, 'graph-extended.json')
graph = GraphCreator()
graph.create_vertices(97)
