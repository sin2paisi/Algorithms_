def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Not found

# Example
arr = [4, 2, 7, 1, 9, 3]
print(linear_search(arr, 7))  # Output: 2