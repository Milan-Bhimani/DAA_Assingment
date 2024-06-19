def check_even_odd(num):
    if num % 2 ==0:
        return 'even'
    else:
        return 'odd'

def check_positive_negative_zero(num):
    if num > 0 :
        return 'positive'
    elif num < 0:
        return 'negative'
    else:
        return 'zero'
num = int(input("Enter a Number:"))
print(check_even_odd(num))
print(check_positive_negative_zero(num))
