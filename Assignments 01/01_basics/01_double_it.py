#Write a program that asks a user to enter a number. 
#Your program will then double that number and print out the result.
# It will repeat that process until the value is 100 or greater.

def main():
    # "Take a number input from the user."
    curr_value = int(input("Enter a number: "))  
    
    # "The loop will run as long as the value is less than 100."
    while curr_value < 100:
        curr_value = curr_value * 2  #"Double the value."
        print(curr_value, end=" ")  # "Print the output (to display in a single line)."

# "Call the main function."
if __name__ == '__main__':
    main()