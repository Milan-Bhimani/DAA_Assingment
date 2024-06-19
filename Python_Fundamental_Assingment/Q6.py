def generate_fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        while len(fibonacci_sequence) < n:
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        return fibonacci_sequence


def main():
   
    try:
        num_terms = int(input("Enter the number of terms: "))
        
        
        fibonacci_sequence = generate_fibonacci(num_terms)
      
        print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_sequence}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
