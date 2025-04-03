#Fill out print_multiple(message, repeats), which takes as parameters a string message to print,
# and an integer repeats number of times to print message. 
#We've written the main() function for you, which prompts the user for a message and a 
#number of repeats.
#Please type a message: Hello! Enter a number of times to repeat your message: 
#6 Hello! Hello! Hello! Hello! Hello! Hello!

def print_multiple(message: str, repeats: int):
    for i in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

# Ensures the main function is executed when the script runs
if __name__ == "__main__":
    main()