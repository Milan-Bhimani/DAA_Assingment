def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        result = lcm(num1, num2)

        print(f"The LCM of {num1} and {num2} is: {result}")

    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
