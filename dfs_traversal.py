class GraphEdge:
    def __init__(self, value, next_edge=None):
        self.value: int = value
        self.next_edge: GraphEdge = next_edge

class Graph:
    def __init__(self, edges, labels):
        self.edges: [GraphEdge] = edges
        self.labels: [int] = labels

    def start_traversal(self, root=0):
        queue: [int] = []
        discovered: [bool] = [False for i in range(len(self.edges))]

        if len(self.edges) > root:
            queue.append(root)
            discovered[root] = True

        while len(queue) > 0:
            top_of_queue = queue.pop()
            self.traverse(top_of_queue, queue, discovered)

    def traverse(self, vertex, queue, discovered):
        current_edge = self.edges[vertex]
        while current_edge != None:
            current_index = current_edge.value
            if not discovered[current_index]:
                queue.append(current_index)
                discovered[current_index] = True
            current_edge = current_edge.next_edge
        self.process_vertex(vertex)

    def process_vertex(self, vertex):
        label = self.labels[vertex]
        print(f'Processing vertex {vertex}: {label}')

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
labels = [101, 234, 96, 382, 9, 2, 3, 10, 72]
graph = Graph(edges, labels)
graph.start_traversal()