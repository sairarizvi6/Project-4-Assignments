#Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, 
#but with a catch. We've written a done() function which returns True with likelihood 
#DONE_LIKELIHOOD -- at each number, before printing the number, you should call done() 
#and check if it returns True or not. If done() returns True, we're done counting, 
#and you should use a return statement to end the chaotic_counting() function execution 
#and resume execution of main(), which will print "I'm done.". We've written main() for you --
#check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() 
#is done with its execution.
#I'm going to count until 10 or until I feel like stopping, 
#whichever comes first. 1 2 3 I'm done.

import random

DONE_LIKELIHOOD = 0.2  # Probability that done() returns True

def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """Counts from 1 to 10, but stops early if done() returns True"""
    for i in range(1, 11):
        if done():
            return  # Stop execution and return to main()
        print(i, end=" ")

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

if __name__ == '__main__':
    main()