def activity_selection(activities):
    # activities = [(start, finish), ...]
    activities.sort(key=lambda x: x[1])  # Sort by finish time
    selected = [activities[0]]
    last_finish = activities[0][1]
    
    for start, finish in activities[1:]:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish
    
    return selected

# Example
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
selected = activity_selection(activities)
print(selected)
# Output: [(1, 4), (5, 7), (8, 11), (12, 16)]