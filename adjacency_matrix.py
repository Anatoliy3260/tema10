class AdjacencyMatrixGraph:
    def __init__(self):
        self.vertices = []
        self.vertex_indices = {}
        self.matrix = []

    def add_vertex(self, vertex):
        if vertex not in self.vertex_indices:
            self.vertex_indices[vertex] = len(self.vertices)
            self.vertices.append(vertex)

            # Добавляем новую строку и столбец
            for row in self.matrix:
                row.append(0)
            self.matrix.append([0] * len(self.vertices))

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertex_indices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_indices:
            self.add_vertex(to_vertex)

        from_idx = self.vertex_indices[from_vertex]
        to_idx = self.vertex_indices[to_vertex]
        self.matrix[from_idx][to_idx] = 1

    def create_from_edges(edges):
        graph = AdjacencyMatrixGraph()
        for from_vertex, to_vertex in edges:
            graph.add_edge(from_vertex, to_vertex)
        return graph

    def __str__(self):
        header = "\t" + "\t".join(self.vertices) + "\n"
        rows = []
        for i, row in enumerate(self.matrix):
            rows.append(f"{self.vertices[i]}\t" + "\t".join(map(str, row)))
        return header + "\n".join(rows)


# Тестирование
if __name__ == "__main__":
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'C')]
    graph = AdjacencyMatrixGraph.create_from_edges(edges)
    print("Adjacency Matrix:")
    print(graph)

    print("\nAdding new edge ('B', 'D'):")
    graph.add_edge('B', 'D')
    print(graph)