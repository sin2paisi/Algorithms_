import heapq
from collections import defaultdict

def dijkstra(graph, start):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while pq:
        curr_dist, node = heapq.heappop(pq)
        if curr_dist > distances[node]:
            continue
        for neighbor, weight in graph[node].items():
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example
graph = defaultdict(dict)
edges = [('A','B',1), ('A','C',4), ('B','C',2), ('B','D',5), ('C','D',1)]
for u, v, w in edges:
    graph[u][v] = w
    graph[v][u] = w  # undirected

print(dijkstra(graph, 'A'))  
# Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}