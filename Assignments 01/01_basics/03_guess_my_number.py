#Guess My Number****I am thinking of a number between 0 and 99... 
#Enter a guess: 50 Your guess is too high
#Enter a new number: 25 Your guess is too low
#Enter a new number: 40 Your guess is too low
#Enter a new number: 45 Your guess is too low
#Enter a new number: 48 Congrats! The number was: 48

import random  #"To generate a random number."

def main():
   #"Choose a random number between 0 and 99."
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # "Take a number input from the user."
        guess = int(input("Enter a guess: "))

        # "Check the conditions."
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  #"End the loop when the correct answer is given."

#"Call the main function."
if __name__ == '__main__':
    main()