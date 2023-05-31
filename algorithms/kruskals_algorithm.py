import json
import os
from os import path

from data.union_find_set import UnionFindSet

class GraphEdge:
    def __init__(self, value, weight, next_edge=None):
        self.value: int = value
        self.weight: int = weight
        self.next_edge: GraphEdge = next_edge

class GraphEdgeItem:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight

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
            graph_edge_weights = graph_data['edge-weights']
            graph_labels = graph_data['labels']

            for index, graph_edge in graph_edges.items():
                graph_label = graph_labels[index]
                graph_edge_weight = graph_edge_weights[index]
                self.add_vertex(graph_label, graph_edge, graph_edge_weight)

    def add_vertex(self, label, edges=None, edge_weights=None):
        self.edges.append(None)
        self.labels.append(label)

        if edges is not None:
            vertex = len(self.edges) - 1
            for index, value in enumerate(edges):
                edge_weight = edge_weights[index]
                self.add_edge(vertex, value, edge_weight)

    def add_edge(self, vertex, value, edge_weight):
        current_edge = self.edges[vertex]
        new_edge = GraphEdge(value, edge_weight, current_edge)
        self.edges[vertex] = new_edge

    def spanning_tree(self, root=0):
        total_vertex_count = len(self.edges)
        union_find_set: UnionFindSet = UnionFindSet(total_vertex_count)
        union_find_vertex_count = 0
        unused_edges = self.load_unused_edges()

        self.begin_processing_tree()
        while union_find_vertex_count < total_vertex_count and len(unused_edges) > 0:
            top_of_stack: GraphEdgeItem = unused_edges.pop()
            if not union_find_set.same_connected_component(top_of_stack.x, top_of_stack.y):
                union_find_set.union(top_of_stack.x, top_of_stack.y)
                self.process_edge(top_of_stack)
            union_find_vertex_count = union_find_set.size[root]

        self.finish_processing_tree(union_find_vertex_count == total_vertex_count)

    def load_unused_edges(self):
        unused_edges: [GraphEdgeItem] = []
        for index, edge in enumerate(self.edges):
            current_edge = edge
            while current_edge is not None:
                current_edge_item = GraphEdgeItem(index, current_edge.value, current_edge.weight)
                unused_edges.append(current_edge_item)
        unused_edges = sorted(unused_edges, key=lambda item: item.weight)
        return unused_edges

    def process_edge(self, edge_item):
        self.weight += edge_item.weight
        print(f'Adding vertex {edge_item.x} to spanning tree, via edge ({edge_item.x}, '
              f' {edge_item.y}). Weight is {edge_item.weight}.')

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
