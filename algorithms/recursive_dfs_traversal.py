import json
import os
from os import path

class GraphEdge:
    def __init__(self, value, next_edge=None):
        self.value: int = value
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

            for index, graph_edge in graph_edges.items():
                graph_label = graph_labels[index]
                self.add_vertex(graph_label, graph_edge)

    def add_vertex(self, label, edges=None):
        self.edges.append(None)
        self.labels.append(label)

        if edges is not None:
            vertex = len(self.edges) - 1
            for edge in edges:
                self.add_edge(vertex, edge)

    def add_edge(self, x, y):
        current_edge = self.edges[x]
        new_edge = GraphEdge(y, current_edge)
        self.edges[x] = new_edge

    def start_traversal(self, root=0):
        discovered: [bool] = [False for i in range(len(self.edges))]
        parent: [int] = [-1 for i in range(len(self.edges))]

        self.traverse(root, discovered, parent)

    def traverse(self, root, discovered, parent):
        discovered[root] = True
        self.start_processing_vertex(root)
        current_element = self.edges[root]
        while current_element is not None:
            current_index = current_element.value
            if not discovered[current_index]:
                parent[current_index] = root
                self.traverse(current_index, discovered, parent)
            current_element = current_element.next_edge
        self.finish_processing_vertex(root)

    def start_processing_vertex(self, vertex):
        label = self.labels[vertex]
        print(f'Begin processing vertex {vertex}: {label}')

    def finish_processing_vertex(self, vertex):
        print(f'Finish processing vertex {vertex}')

def define_edges() -> [GraphEdge]:
    edge_0 = GraphEdge(3)
    edge_0.next_edge = GraphEdge(5)
    edge_0.next_edge.next_edge = GraphEdge(6)
    edge_0.next_edge.next_edge.next_edge = GraphEdge(2)

    edge_1 = GraphEdge(4)
    edge_1.next_edge = GraphEdge(2)
    edge_1.next_edge.next_edge = GraphEdge(3)
    edge_1.next_edge.next_edge.next_edge = GraphEdge(7)

    edge_2 = GraphEdge(8)
    edge_2.next_edge = GraphEdge(0)
    edge_2.next_edge.next_edge = GraphEdge(1)
    edge_2.next_edge.next_edge.next_edge = GraphEdge(6)

    edge_3 = GraphEdge(7)

    edge_4 = GraphEdge(2)

    edge_5 = GraphEdge(8)
    edge_5.next_edge = GraphEdge(2)
    edge_5.next_edge.next_edge = GraphEdge(1)
    edge_5.next_edge.next_edge.next_edge = GraphEdge(7)
    edge_5.next_edge.next_edge.next_edge.next_edge = GraphEdge(0)
    edge_5.next_edge.next_edge.next_edge.next_edge.next_edge = GraphEdge(4)

    edge_6 = GraphEdge(3)
    edge_6.next_edge = GraphEdge(1)

    edge_7 = GraphEdge(4)
    edge_7.next_edge = GraphEdge(1)

    edge_8 = GraphEdge(2)

    edges = [edge_0, edge_1, edge_2, edge_3, edge_4, edge_5, edge_6, edge_7, edge_8]
    return edges

# Entrypoint
parent_directory = path.dirname(os.getcwd())
graph_file = path.join(parent_directory, 'data', 'graph.json')
graph = Graph(graph_file)
graph.start_traversal()
