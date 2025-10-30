# selection_sort.py
def selection_sort(arr):
    """Selection Sort - Find minimum and place in correct position."""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Test
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", data)
    print("Sorted:  ", selection_sort(data.copy()))