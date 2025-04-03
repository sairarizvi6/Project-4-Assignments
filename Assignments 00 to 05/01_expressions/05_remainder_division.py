
#Ask the user for two numbers, one at a time, and then print the result of dividing 
#the first number by the second and also the remainder of the division.
#Please enter an integer to be divided: 5
#Please enter an integer to divide by: 3
#The result of this division is 1 with a remainder of 2

def main():
    # Prompt the user to enter the dividend (the number to be divided)
    dividend: int = int(input("Please enter an integer to be divided: "))

    # Prompt the user to enter the divisor (the number to divide by)
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Calculate the quotient using integer division (//)
    quotient: int = dividend // divisor  

    # Calculate the remainder using the modulus operator (%)
    remainder: int = dividend % divisor  

    # Display the result of the division
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

# Call the main function to execute the program
main()
