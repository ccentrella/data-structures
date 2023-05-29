import json
import os
import sys
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
        self.weight: int = 0

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

    def spanning_tree(self, root=0):
        if len(self.edges) <= root:
            return

        tree: [int] = [root]
        connected: bool = True
        self.begin_processing_tree()
        while len(tree) < len(self.edges):
            optimal_vertex, optimal_edge = self.next_vertex(tree)
            if optimal_vertex != -1:
                tree.append(optimal_vertex)
                self.process_edge(optimal_vertex, optimal_edge)
            else:
                connected = False
                break
        self.finish_processing_tree(connected)

    def next_vertex(self, tree) -> (int, GraphEdge):
        optimal_vertex: int = -1
        optimal_edge: GraphEdge = GraphEdge(tree[0], sys.maxsize)
        for index, graph_edge in enumerate(self.edges):
            if index in tree:
                continue
            current_edge = graph_edge
            while current_edge is not None:
                current_value = current_edge.value
                if current_value in tree and current_edge.weight < optimal_edge.weight:
                    optimal_vertex = index
                    optimal_edge = current_edge
                current_edge = current_edge.next_edge

        return optimal_vertex, optimal_edge

    def process_edge(self, x, edge):
        y = edge.value
        weight = edge.weight
        self.weight += weight
        print(f'Adding vertex {x} to spanning tree, via edge ({x}, {y}). Weight is {weight}.')

    def begin_processing_tree(self):
        self.weight = 0
        print(f'Creating spanning tree...\n')

    def finish_processing_tree(self, connected):
        print(f'\nSpanning tree created successfully.')
        print(f'Total weight: {self.weight}')

        if not connected:
            print('Warning: The input graph was not connected, so some vertices weren\'t included.')

parent_directory = path.dirname(os.getcwd())
graph_file = path.join(parent_directory, 'data', 'graph_one_thousand.json')
graph = Graph(graph_file)
graph.spanning_tree()
