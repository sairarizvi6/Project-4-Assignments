#Simulate rolling two dice, three times. Prints the results of each die roll. 
#This program is used to show how variable scope works.


import random

one_side = 6  # Number of sides on the dice

def roll_dice():
    die1 = random.randint(1, one_side)
    die2 = random.randint(1, one_side)
    total = die1 + die2
    print(f"Rolled: {die1} and {die2} -> Total: {total}")

def main():
    die1 = 10  # Local variable in main()
    print(f"die1 in main() starts as: {die1}")
    
    for _ in range(3):  # Roll dice three times
        roll_dice()
    
    print(f"die1 in main() ends as: {die1}")

main()
