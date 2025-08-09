from collections import deque

def bfs(graph, start_vertex):
    """
    Универсальный BFS для всех типов представления графа
    """
    # Определяем тип графа и получаем его представление в стандартном виде
    graph_type, standardized_graph = standardize_graph(graph)

    # Проверяем наличие стартовой вершины
    if start_vertex not in {v for v, _ in standardized_graph}:
        return []

    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    result = []

    while queue:
        current_vertex = queue.popleft()
        result.append(current_vertex)

        # Получаем соседей из стандартизированного представления
        neighbors = [n for v, n in standardized_graph if v == current_vertex]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def standardize_graph(graph):
    
    standardized = []

    # 1. DirectedGraph
    if hasattr(graph, 'vertices') and isinstance(graph.vertices, dict):
        for v, neighbors in graph.vertices.items():
            standardized.extend((v, n) for n in neighbors)
        return ('DirectedGraph', standardized)

    # 2. Список смежности (dict)
    elif isinstance(graph, dict):
        for v, neighbors in graph.items():
            standardized.extend((v, n) for n in neighbors)
        return ('AdjacencyList', standardized)

    # 3. Матрица смежности
    elif hasattr(graph, 'matrix') and hasattr(graph, 'vertex_indices'):
        vertices = list(graph.vertex_indices.keys())
        for i, row in enumerate(graph.matrix):
            v = vertices[i]
            standardized.extend((v, vertices[j]) for j, val in enumerate(row) if val == 1)
        return ('AdjacencyMatrix', standardized)

    # 4. Список рёбер
    elif isinstance(graph, (list, tuple)) and all(isinstance(e, (list, tuple)) and len(e) == 2 for e in graph):
        return ('EdgeList', graph)

    raise ValueError("Неподдерживаемый тип представления графа")


if __name__ == "__main__":
    # Тест 1: Список смежности (dict)
    adj_list = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': ['E'],
        'E': []
    }
    print("BFS (список смежности):", bfs(adj_list, 'A'))

    # Тест 2: DirectedGraph
    try:
        from directed_graph import DirectedGraph

        dg = DirectedGraph()
        dg.add_edge('A', 'B')
        dg.add_edge('A', 'C')
        dg.add_edge('B', 'D')
        dg.add_edge('C', 'E')
        dg.add_edge('D', 'E')
        print("BFS (DirectedGraph):", bfs(dg, 'A'))
    except ImportError:
        print("Модуль directed_graph не найден")

    # Тест 3: Матрица смежности
    try:
        from adjacency_matrix import AdjacencyMatrixGraph

        amg = AdjacencyMatrixGraph()
        amg.add_edge('A', 'B')
        amg.add_edge('A', 'C')
        amg.add_edge('B', 'D')
        amg.add_edge('C', 'E')
        amg.add_edge('D', 'E')
        print("BFS (матрица смежности):", bfs(amg, 'A'))
    except ImportError:
        print("Модуль adjacency_matrix не найден")

    # Тест 4: Список рёбер
    edge_list = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'E')]
    print("BFS (список рёбер):", bfs(edge_list, 'A'))