#Use Python to calculate the number of seconds in a year, 
#and tell the user what the result is in a nice print statement that looks like this
# (of course the value 5 should be the calculated number instead):
#There are 5 seconds in a year!
#You should use constants for this exercise -- 
#there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, 
#and 60 seconds per minute.


# Useful constants to help make the math easier and cleaner!
DAYS_PER_YEAR: int = 365  # Number of days in a year
HOURS_PER_DAY: int = 24   # Number of hours in a day
MIN_PER_HOUR: int = 60    # Number of minutes in an hour
SEC_PER_MIN: int = 60     # Number of seconds in a minute

def main():
    # Calculate the total number of seconds in a year
    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Print the result
    print("There are " + str(total_seconds) + " seconds in a year!")

# Call the main function to execute the program
main()
