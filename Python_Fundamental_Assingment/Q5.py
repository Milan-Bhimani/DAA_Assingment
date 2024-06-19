def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    
    try:
        num = int(input("Enter an integer: "))
        
        if is_prime(num):
            print(f"The number {num} is prime.")
        else:
            print(f"The number {num} is not prime.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
