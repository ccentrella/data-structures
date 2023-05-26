class GraphVertex:
    def __init__(self, value, next_element=None):
        self.value: int = value
        self.next_element: GraphVertex = next_element

class Graph:
    def __init__(self, vertices):
        self.vertices: [GraphVertex] = vertices

    def start_traversal(self, root=0):
        queue: [GraphVertex] = []
        discovered: [bool] = [False for i in range(len(self.vertices))]
        parent: [int] = [0 for i in range(len(self.vertices))]

        if len(self.vertices) > root:
            root_element = self.vertices[root]
            queue.append(root_element)
            discovered[root] = True
            parent[root_element.value] = root

        while len(queue) > 0:
            current_element = queue.pop()
            self.traverse(current_element, queue, discovered, parent)

    def traverse(self, current_element, queue, discovered, parent):
        parent_index = parent[current_element.value]
        self.process_edge(parent_index, current_element.value)

        next_element = current_element
        while next_element is not None:
            next_index = next_element.value
            if not discovered[next_index]:
                queue.append(next_element)
                discovered[next_index] = True
                parent[parent_index] = next_element.value
            parent_index = next_element.value
            next_element = next_element.next_element

    def process_edge(self, x, y):
        print(f'Processing edge: ({x}, {y})')

def define_vertexes() -> [GraphVertex]:
    vertex_1 = GraphVertex(0)
    vertex_1.next_element = GraphVertex(5)
    vertex_1.next_element.next_element = GraphVertex(6)
    vertex_1.next_element.next_element.next_element = GraphVertex(2)

    vertex_2 = GraphVertex(4)
    vertex_2.next_element = GraphVertex(2)
    vertex_2.next_element.next_element = GraphVertex(3)
    vertex_2.next_element.next_element.next_element = GraphVertex(7)

    vertex_3 = GraphVertex(8)
    vertex_3.next_element = GraphVertex(2)
    vertex_3.next_element.next_element = GraphVertex(1)
    vertex_3.next_element.next_element.next_element = GraphVertex(6)

    vertex_4 = GraphVertex(7)

    vertex_5 = GraphVertex(2)

    vertex_6 = GraphVertex(8)
    vertex_6.next_element = GraphVertex(2)
    vertex_6.next_element.next_element = GraphVertex(1)
    vertex_6.next_element.next_element.next_element = GraphVertex(7)
    vertex_6.next_element.next_element.next_element.next_element = GraphVertex(0)
    vertex_6.next_element.next_element.next_element.next_element.next_element = GraphVertex(1)

    vertex_7 = GraphVertex(3)
    vertex_7.next_element = GraphVertex(1)

    vertex_8 = GraphVertex(4)
    vertex_8.next_element = GraphVertex(7)

    vertex_9 = GraphVertex(2)

    vertexes = [vertex_1, vertex_2, vertex_3, vertex_4, vertex_5, vertex_6, vertex_7, vertex_8, vertex_9]
    return vertexes

# Entry point
vertices = define_vertexes()
graph = Graph(vertices)
graph.start_traversal()