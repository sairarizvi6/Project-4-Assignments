#Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
#Prompt the user to enter the first number.
#Read the input and convert it to an integer.
#Prompt the user to enter the second number.
#Read the input and convert it to an integer.
#Calculate the sum of the two numbers.
#Print the total sum with an appropriate message.

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        result = num1 + num2
        print(f"Sum: {num1} + {num2} = {result}")
    
    except ValueError:
        print("Error! Please enter valid numbers.")

main()


