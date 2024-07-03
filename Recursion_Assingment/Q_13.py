def pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / pow(x, -n)
    if n % 2 == 0:
        half_pow = pow(x, n // 2)
        return half_pow * half_pow
    else:
        return x * pow(x, n - 1)
print(pow(2, 10)) 
print(pow(2, -2)) 
print(pow(3, 5))   
print(pow(5, 0))   
