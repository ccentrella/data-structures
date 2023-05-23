vertices = [(0, 240, 0), (204, 240, 0), (204, 0, 0), (0, 0, 0)]
triangles = [(0, 1, 3), (1, 2, 3)]
vertex_triangles = [set() for i in range(len(vertices))]

def generate_triangles_by_vertex() -> None:
    for index, triangle in enumerate(triangles):
        x, y, z = triangle
        vertex_triangles[x].add(index)
        vertex_triangles[y].add(index)
        vertex_triangles[z].add(index)

def generate_dual_graph() -> []:
    matches = set()
    for index, triangle in enumerate(triangles):
        candidates = {}
        x, y, z = triangle

        for vertex_triangle in vertex_triangles[x]:
            count = candidates.setdefault(vertex_triangle, 0)
            candidates[vertex_triangle] = count + 1
        for vertex_triangle in vertex_triangles[y]:
            count = candidates.setdefault(vertex_triangle, 0)
            candidates[vertex_triangle] = count + 1
        for vertex_triangle in vertex_triangles[z]:
            count = candidates.setdefault(vertex_triangle, 0)
            candidates[vertex_triangle] = count + 1

        for candidate in candidates:
            if candidates[candidate] > 1:
                matches.add(candidate)

    return matches

# Entrypoint
generate_triangles_by_vertex()
adjacent_triangles = generate_dual_graph()
print(adjacent_triangles)
