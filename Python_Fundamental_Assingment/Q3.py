def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    
    try:
        num = int(input("Enter a non-negative integer: "))
        
        
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
           
            result = factorial(num)
            
            
            print(f"The factorial of {num} is {result}.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
