class DirectedGraph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertices:
            self.add_vertex(to_vertex)

        self.vertices[from_vertex].append(to_vertex)
        self.edges.append((from_vertex, to_vertex))

    def __str__(self):
        return f"Vertices: {list(self.vertices.keys())}\nEdges: {self.edges}"


# Тестирование
if __name__ == "__main__":
    graph = DirectedGraph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'A')
    graph.add_edge('A', 'C')

    print(graph)