def sum_of_digits(n):
    
    n_str = str(n)
    total = 0
    for digit in n_str:
        total += int(digit)
    return total

def main():

    try:
        num = int(input("Enter an integer: "))
        
   
        digit_sum = sum_of_digits(num)
      
        print(f"The sum of the digits of {num} is {digit_sum}.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
