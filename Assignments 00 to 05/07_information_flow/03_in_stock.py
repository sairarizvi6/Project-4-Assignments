#Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit
# as a parameter and returns how many of that fruit are in her inventory. 
#Write code in main() which will:
#Prompt the user to enter a fruit ("Enter a fruit: ")
#Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock
#Print the number which are in stock if Sophia has that fruit in her inventory 
# (there are more than 0 in stock)
#Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.
#Enter a fruit: pear
#This fruit is in stock! Here is how many:1000
#Enter a fruit: lychee
#This fruit is not in stock.

# Function to check the stock of a given fruit
def num_in_stock(fruit):
    inventory = {
        "apple": 500,
        "banana": 300,
        "pear": 1000,
        "orange": 250,
        "mango": 700
    }
    return inventory.get(fruit.lower(), 0)  # Return stock count or 0 if not found

def main():
    # Prompt the user for input
    fruit = input("Enter a fruit: ").strip()

    # Get the number of fruit in stock
    stock = num_in_stock(fruit)

    # Print appropriate message based on stock availability
    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

# Required line to run the program
if __name__ == '__main__':
    main()