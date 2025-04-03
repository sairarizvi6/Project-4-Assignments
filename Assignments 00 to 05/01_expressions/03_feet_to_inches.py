
#Converts feet to inches. Feet is an American unit of measurement. 
#There are 12 inches per foot. Foot is the singular, and feet is the plural.


# Define the number of inches in one foot (constant)
INCHES_IN_FOOT: int = 12

# Main function to convert feet to inches
def main():
    # Prompt the user to input the number of feet
    feet: float = float(input("Enter number of feet: "))
    
    # Convert feet to inches using the conversion factor
    inches: float = feet * INCHES_IN_FOOT
    
    # Display the result
    print("That is", inches, "inches!")

# Call the main function to execute the program
main()
