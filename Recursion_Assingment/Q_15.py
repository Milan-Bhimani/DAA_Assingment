def is_power_of_three(n):
    if n == 1:
        return True
    if n <= 0 or n % 3 != 0:
        return False
    return is_power_of_three(n // 3)

print(is_power_of_three(1))   
print(is_power_of_three(3))    
print(is_power_of_three(9))    
print(is_power_of_three(27))   
print(is_power_of_three(10))   
print(is_power_of_three(0))    
print(is_power_of_three(-3))   
