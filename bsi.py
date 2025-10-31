def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example
sorted_arr = [2, 3, 4, 10, 40]
print(binary_search_iterative(sorted_arr, 10))  # Output: 3