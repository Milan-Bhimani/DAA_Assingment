def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


def main():
    
    try:
        num = int(input("Enter a positive integer: "))
        
       
        if num <= 0:
            print("Please enter a positive integer.")
        else:

            factors = find_factors(num)
            
            
            print(f"The factors of {num} are: {factors}")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
