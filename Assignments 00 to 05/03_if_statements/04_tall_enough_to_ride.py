def main():
    while True:
        # Take height input from the use
        height = input("How tall are you? ")

        #If the user presses enter without input, the program should stop.
        if height == "":
            print("Exiting the program. Have a great day!")
            break

        # Convert input to a number
        height = int(height)

        # Check height
        if height >= 50:
            print("You're tall enough to ride!\n")
        else:
            print("You're not tall enough to ride, but maybe next year!\n")

# This line is necessary to run the program.
if __name__ == '__main__':
    main()