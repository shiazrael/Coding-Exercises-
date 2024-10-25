# -*- coding: utf-8 -*-
"""
Exercise 10: Is it even? - 35 Marks
"""
def check_even_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    user_input = int(input("Please enter a number: "))  # Ask for user input
    result = check_even_odd(user_input)  # Call the function
    print(result)  # Print the result

if __name__ == "__main__":
    main()