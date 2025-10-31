def power(base, exp)
    if exp == 0
        return 1
    if exp  0
        return 1  power(base, -exp)
    
    half = power(base, exp  2)
    if exp % 2 == 0
        return half  half
    else
        return base  half  half

# Example
print(power(2, 10))   # Output 1024
print(power(3, 5))    # Output 243