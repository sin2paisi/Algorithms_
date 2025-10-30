# counting_sort.py
def counting_sort(arr):
    """Counting Sort - For integers with known range. Non-comparison sort."""
    if not arr:
        return arr
    
    # Find range of input
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Create count array
    count = [0] * range_val
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Build output array (from end for stability)
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1
    
    return output

# Test
if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print("Original:", data)
    print("Sorted:  ", counting_sort(data))