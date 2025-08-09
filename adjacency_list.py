class AdjacencyListGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.adj_list:
            self.add_vertex(from_vertex)
        if to_vertex not in self.adj_list:
            self.add_vertex(to_vertex)

        self.adj_list[from_vertex].append(to_vertex)

    def create_from_edges(edges):
        graph = AdjacencyListGraph()
        for from_vertex, to_vertex in edges:
            graph.add_edge(from_vertex, to_vertex)
        return graph

    def __str__(self):
        return "\n".join(
            f"{vertex}: {neighbors}"
            for vertex, neighbors in self.adj_list.items()
        )


# Тестирование
if __name__ == "__main__":
    edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'C')]
    graph = AdjacencyListGraph.create_from_edges(edges)
    print("Adjacency List:")
    print(graph)

    print("\nAdding new edge ('B', 'D'):")
    graph.add_edge('B', 'D')
    print(graph)