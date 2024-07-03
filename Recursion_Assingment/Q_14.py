def is_power_of_two(n):
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

print(is_power_of_two(1))  
print(is_power_of_two(2))   
print(is_power_of_two(3))   
print(is_power_of_two(4))    
print(is_power_of_two(16))  
print(is_power_of_two(18))  
