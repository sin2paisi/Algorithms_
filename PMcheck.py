def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
print(is_prime(17))  # Output: True
print(is_prime(4))   # Output: False