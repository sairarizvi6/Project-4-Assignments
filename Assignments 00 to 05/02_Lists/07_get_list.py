#Write a program which continuously asks the user to enter values which are added 
#one by one into a list. When the user presses enter without typing anything,
# print the list.Enter a value: 
#1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def main():
    lst = []  # Empty list to store user inputs
    
    while True:
        value = input("Enter a value: ")  # Taking input from user
        
        if value == "":  # If user presses enter without typing anything, exit loop
            break
        
        lst.append(value)  # Adding value to the list

    print("Here's the list:", lst)  # Printing the final list

# Required line to run the program
if __name__ == '__main__':
    main()