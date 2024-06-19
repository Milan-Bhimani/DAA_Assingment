def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    return sorted(str1) == sorted(str2)

def main():
    try:
        str1 = input("Enter the first string: ")
        str2 = input("Enter the second string: ")
        
        if are_anagrams(str1, str2):
            print(f'"{str1}" and "{str2}" are anagrams.')
        else:
            print(f'"{str1}" and "{str2}" are not anagrams.')
    except ValueError:
        print("Please enter valid strings.")

if __name__ == "__main__":
    main()
