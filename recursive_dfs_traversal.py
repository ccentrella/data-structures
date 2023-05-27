class GraphEdge:
    def __init__(self, value, next_edge=None):
        self.value: int = value
        self.next_edge: GraphEdge = next_edge

class Graph:
    def __init__(self, edges, labels):
        self.edges: [GraphEdge] = edges
        self.labels: [int] = labels

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
edges = define_edges()
labels = [6, 23, 9235, 239, 92, 256, 88, 6, 120]
graph = Graph(edges, labels)
graph.start_traversal()
