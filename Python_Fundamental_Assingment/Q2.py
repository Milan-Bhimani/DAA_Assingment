def sum_of_natural_numbers(N):
    return N * (N + 1) // 2
def main():
    try:
        N = int(input("Enter a positive integer N: "))
        if N <= 0:
            print("Please enter a positive integer.")
        else:
            sum_N = sum_of_natural_numbers(N)
            print(f"The sum of the first {N} natural numbers is {sum_N}.")
    except ValueError:
        print("Please enter a valid integer.")
if __name__ == "__main__":
    main()
