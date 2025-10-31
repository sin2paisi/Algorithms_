def find_max(arr):
    if not arr:
        return None
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Example
print(find_max([3, 7, 2, 9, 1]))  # Output: 9