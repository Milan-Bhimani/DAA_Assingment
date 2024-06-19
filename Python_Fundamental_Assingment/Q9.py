def is_armstrong_number(n):
    
    num_str = str(n)
    num_digits = len(num_str)
    
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    return total == n

def main():
    
    try:
        num = int(input("Enter an integer: "))
        
        
        if is_armstrong_number(num):
            print(f"The number {num} is an Armstrong number.")
        else:
            print(f"The number {num} is not an Armstrong number.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
