def get_integer_input() -> int:

    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:

    return f"{number} is an {'Even' if number % 2 == 0 else 'Odd'} number."

def main() -> None:

    number = get_integer_input()  # Get valid integer input from the user
    result = check_even_odd(number)  # Determine if the number is even or odd
    print(result)  # Display the result to the user

if __name__ == "__main__":
    main()