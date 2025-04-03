
#Simulate rolling two dice, and prints results of each roll as well as the total.

import random  # Import the random module for generating random numbers

# Define the number of sides on a die
one_side = 6

# Function to roll two dice and display their sum
def roll_dice():
    die1 = random.randint(1, one_side)  # Generate a random number between 1 and 6 for the first die
    die2 = random.randint(1, one_side)  # Generate a random number between 1 and 6 for the second die
    total = die1 + die2  # Calculate the sum of the two dice
    print(f"Total of the two dice: {total}")  # Print the total

# Main function to demonstrate variable scope and call roll_dice()
def main():
    die1 = 10  # Local variable die1 in main()
    print("die1 in main() starts as: " + str(die1))  # Print the initial value of die1 in main()

    # Call roll_dice() three times
    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() ends as: " + str(die1))  # Print the value of die1 in main() after calling roll_dice()

# Call the main function to execute the program
main()
