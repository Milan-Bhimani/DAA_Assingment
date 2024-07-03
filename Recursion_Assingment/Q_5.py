def decimal_to_binary(n):
    if n > 1:
        decimal_to_binary(n // 2)
    print(n % 2, end='')

# Test the function
decimal_to_binary(3)
print() 