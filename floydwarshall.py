def floyd_warshall(graph):
    V = len(graph)
    dist = [[float('infinity')] * V for _ in range(V)]
    nodes = list(graph.keys())
    node_to_idx = {node: i for i, node in enumerate(nodes)}
    
    # Initialize distances
    for u in graph:
        i = node_to_idx[u]
        dist[i][i] = 0
        for v, weight in graph[u].items():
            j = node_to_idx[v]
            dist[i][j] = weight
    
    # Dynamic programming
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return {nodes[i]: {nodes[j]: dist[i][j] for j in range(V)} for i in range(V)}

# Example
graph = {
    0: {1: 4, 2: 2},
    1: {3: 1},
    2: {1: 1, 3: 5},
    3: {}
}
print(floyd_warshall(graph))