def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 1:
                return False
        # Check upper-left diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 1:
                return False
        # Check upper-right diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 1:
                return False
        return True
    
    def backtrack(row):
        if row == n:
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0  # backtrack
    
    backtrack(0)
    return solutions

# Example (N=4)
solutions = solve_n_queens(4)
print(f"Found {len(solutions)} solutions for N=4")
for sol in solutions[:1]:  # Print first solution
    for row in sol:
        print(row)
# Output: One valid configuration