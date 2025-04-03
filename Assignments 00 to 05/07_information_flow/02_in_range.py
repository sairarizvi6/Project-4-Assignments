#Implement the following function which takes in 3 integers as parameters:
#def in_range(n, low, high) """ Returns True if n is between low and high, 
#inclusive. high is guaranteed to be greater than low. """



def in_range(n, low, high):
    """Returns True if n is between low and high (inclusive)."""
    return low <= n <= high

def main():
    # Ask the user for input
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower limit: "))
    high = int(input("Enter the upper limit: "))

    # Call the in_range function and print the result
    result = in_range(n, low, high)
    print(result)

# Required line to run the program
if __name__ == '__main__':
    main()