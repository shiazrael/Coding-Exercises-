# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:07:52 2024

@author: Matthew Flores
"""

def search_string(target, string_list):
    # Define a function to search for a target string in a list of strings
    indices = []  # Initialize a list to hold the indices of found occurrences
    
    for index, string in enumerate(string_list):  # Loop through the list with index
        # Check if the target string is present in the current string
        if target in string:
            # If the target is found, append the current index to the indices list
            indices.append(index)
    
    return indices  # Return the list of found indices

def main():
    # Define the main function to execute the program
    strings = [  # Initialize a sample list of strings to search within
        "Jake",  # First string
        "Zac",  # Second string
        "Ian",  # Third string
        "Ron",  # Fourth string
        "Sam"  # Fifth string
        "Dave"  # Sixth string   
        ]
    
    # Prompt the user for the string to search for
    target_string = input("Enter the string to search for: ")
    
    # Call the search function to find occurrences of the target string
    found_indices = search_string(target_string, strings)
    
    # Check if any indices were found
    if found_indices:
        # If found, print the target string and its found indices
        print(f"The string '{target_string}' was found at indices: {found_indices}")
    else:
        # If not found, inform the user that the string was not found
        print(f"The string '{target_string}' was not found in the list.")

# Standard Python convention to run the main function when the script is executed
if __name__ == "__main__":
    main()  # Call the main function to start the program