class UnionFindSet:
    def __init__(self, total_vertices):
        self.size: [int] = [1 for i in range(total_vertices)]
        self.parent: [int] = [i for i in range(total_vertices)]

    def find_root(self, vertex):
        if self.parent[vertex] == vertex:
            return vertex
        else:
            return self.find_root(self.parent[vertex])

    def same_connected_component(self, x, y) -> bool:
        root_x = self.find_root(x)
        root_y = self.find_root(y)

        return root_x == root_y

    def union(self, x, y):
        root_x = self.find_root(x)
        root_y = self.find_root(y)

        if root_x == root_y:
            return
        elif root_x < root_y:
            self.size[root_y] += self.size[root_x]
            self.parent[root_x] = root_y
        else:
            self.size[root_x] += self.size[root_y]
            self.parent[root_y] = root_x

union_find_set = UnionFindSet(50)
print(union_find_set.size)
print(union_find_set.parent)
