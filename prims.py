import heapq

def prim(graph, start):
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (weight, node, parent)
    total_cost = 0
    
    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        if parent is not None:
            mst.append((parent, node, weight))
            total_cost += weight
        for neighbor, w in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (w, neighbor, node))
    
    return mst, total_cost

# Example
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 3},
    'D': {'B': 1, 'C': 3}
}
mst, cost = prim(graph, 'A')
print("MST:", mst)      # e.g., [('A', 'B', 2), ('B', 'C', 1), ('B', 'D', 1)]
print("Cost:", cost)    # Output: 4