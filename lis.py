def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    tails = [arr[0]]
    for num in arr[1:]:
        if num > tails[-1]:
            tails.append(num)
        else:
            # Binary search to find position to replace
            left, right = 0, len(tails) - 1
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = num
    return len(tails)

# Example
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subsequence(arr))  # Output: 4 (e.g., [2, 3, 7, 18])