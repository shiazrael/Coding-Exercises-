# -*- coding: utf-8 -*-
"""
Exercise 5: Days of the Month - 30 Marks
"""

days_in_month_dict = {
    "January": 31,
    "February": 28,  # This is the standard number of days in February
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    """Return the number of days in a given month of a given year."""
    # Check for leap year and February
    if is_leap_year(year) and month == "February":
        return 29  # Leap year February has 29 days

    try:
        return days_in_month_dict[month]  # Return days from the dictionary
    except KeyError:
        return None  # Return None if the month is invalid

# Example usage
if __name__ == "__main__":
    year = int(input("Enter a year: "))
    month = input("Enter a month: ")

    days = days_in_month(year, month)
    if days is not None:
        print(f"{month} {year} has {days} days.")
    else:
        print("Invalid month entered.")