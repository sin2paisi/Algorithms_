def bellman_ford(graph, source):
    V = len(graph)
    dist = {node: float('infinity') for node in graph}
    dist[source] = 0
    
    # Relax edges |V|-1 times
    for _ in range(V - 1):
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
    
    # Check for negative cycles
    for u in graph:
        for v, weight in graph[u].items():
            if dist[u] + weight < dist[v]:
                raise ValueError("Graph contains a negative cycle")
    
    return dist

# Example
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
print(bellman_ford(graph, 'A'))
# Output: {'A': 0, 'B': -1, 'C': 2, 'D': -2, 'E': 1}