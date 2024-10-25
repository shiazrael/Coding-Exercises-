# -*- coding: utf-8 -*-
"""
Exercise 6: Brute Force Attack - 30 Marks
"""
#Define the correct password as a string
password = "12345"  
# Initialize the user input variable for the password
passwordinput = ""  
# Set the maximum number of attempts allowed
attempt = 5  

# Start a loop that continues until the correct password is entered or attempts run out
while passwordinput != password and attempt > 0:
    # Print the number of attempts left for the user
    print(f"Your current attempts left: {attempt}")
    # Prompt the user to input the password
    passwordinput = input("Password: ")  # Input should be a string
    # Decrease the number of attempts by 1
    attempt -= 1  

    # Check if the entered password is incorrect
    if passwordinput != password:
        # Inform the user that the password is incorrect
        print("Incorrect password. Please try again.")

    # Check if the user has used all attempts
    if attempt == 0:
        # Inform the user that authorities are coming
        print("The authorities are coming.")
    

