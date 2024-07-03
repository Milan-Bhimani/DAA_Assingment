def recursive_multiply(x, y):
    if y == 0:
        return 0
    if y < 0:
        return -recursive_multiply(x, -y)
    return x + recursive_multiply(x, y - 1)

print(recursive_multiply(5, 3))  
print(recursive_multiply(-5, 3)) 
print(recursive_multiply(5, -3)) 
print(recursive_multiply(-5, -3))
print(recursive_multiply(5, 0)) 
