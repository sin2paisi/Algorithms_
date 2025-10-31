"""
0/1 Knapsack Problem (Dynamic Programming Approach)

Problem:
Given weights and values of n items, put these items in a knapsack
of capacity W to get the maximum total value in the knapsack.

- Type: Optimization (Dynamic Programming)
- Time Complexity: O(n * W)
- Space Complexity: O(n * W)
- Stable: Not applicable

"""

from typing import List, Tuple


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Solves the 0/1 Knapsack problem using dynamic programming.

    Args:
        weights: List of item weights.
        values: List of item values.
        capacity: Maximum weight the knapsack can carry.

    Returns:
        The maximum total value that can be accommodated in the knapsack.
    """
    n = len(values)
    # dp[i][w] = max value for first i items with weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Option 1: include item
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                # Option 2: exclude item
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def main():
    """
    Driver function for the 0/1 Knapsack demonstration.
    """
    print("=== 0/1 Knapsack Problem ===")

    # Example input
    n = int(input("Enter number of items: "))
    weights = list(map(int, input("Enter item weights: ").split()))
    values = list(map(int, input("Enter item values: ").split()))
    capacity = int(input("Enter knapsack capacity: "))

    # Validation
    if len(weights) != n or len(values) != n:
        print("Error: Number of weights and values must match number of items.")
        return

    max_value = knapsack(weights, values, capacity)
    print(f"\nMaximum achievable value: {max_value}")


if __name__ == "__main__":
    main()
