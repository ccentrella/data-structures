import json
import os
import random
from os import path

class GraphCreator:
    def __init__(self, file_location=None):
        self.graph_edges = {}
        self.graph_edge_weights = {}
        self.labels = {}

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
        self.create_edge_weights(maximum_weight)
        self.create_labels()

    def create_edges(self, vertex_count, maximum_edges):
        self.begin_processing_edges()
        self.graph_edges = {}
        for index in range(vertex_count):
            edges = []
            edge_count = random.randint(1, maximum_edges)
            for edge_index in range(edge_count):
                random_vertex = random.randint(0, vertex_count - 1)
                edges.append(random_vertex)
            print(f'\"{index}\": {edges},')
            self.graph_edges[index] = edges
        self.finish_processing_edges()

    def create_edge_weights(self, maximum_weight=2000):
        self.begin_processing_edge_weights()
        self.graph_edge_weights = {}
        for index, graph_edge in self.graph_edges.items():
            length = len(graph_edge)
            weights = []
            for i in range(length):
                random_int = random.randint(0, maximum_weight)
                weights.append(random_int)
            print(f'\"{index}\": {weights},')
            self.graph_edge_weights[index] = weights
        self.finish_processing_edge_weights()

    def create_labels(self, maximum_value):
        self.begin_processing_labels()
        self.labels = {}
        for index in self.graph_edges:
            while True:
                random_int = random.randint(1, maximum_value)
                if (random_int % 5 == 0) and (random_int not in self.labels.values()):
                    break
            print(f'\"{index}\": {random_int},')
            self.labels[index] = random_int
        self.finish_processing_labels()

    @staticmethod
    def begin_processing_edges():
        print("Creating edges...\n")

    @staticmethod
    def finish_processing_edges():
        print("\nEdges created successfully.\n")

    @staticmethod
    def begin_processing_edge_weights():
        print("Creating edge weights...\n")

    @staticmethod
    def finish_processing_edge_weights():
        print("\nEdge weights created successfully.\n")

    @staticmethod
    def begin_processing_labels():
        print("Creating labels...\n")

    @staticmethod
    def finish_processing_labels():
        print("\nLabels created successfully.\n")

parent_directory = os.getcwd()
graph_file = path.join(parent_directory, 'graph-extended.json')
graph = GraphCreator(graph_file)
graph.create_labels(1200)