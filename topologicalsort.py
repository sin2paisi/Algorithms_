from collections import defaultdict, deque

def topological_sort(graph):
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    queue = deque([node for node in indegree if indegree[node] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return order if len(order) == len(graph) else []  # Empty if cycle exists

# Example
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}
print(topological_sort(graph))  # Possible Output: ['A', 'B', 'C', 'D', 'E', 'F']