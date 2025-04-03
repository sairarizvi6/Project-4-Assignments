#Fill out the function shorten(lst) which removes elements from the end of lst, 
#which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
# If lst is already shorter than MAX_LENGTH you should leave it unchanged. 
#For the autograder to pass you will need MAX_LENGTH to be 3, 
#but feel free to change it around to test your program.

MAX_LENGTH = 3  # Define the maximum allowed length

def shorten(lst):
    while len(lst) > MAX_LENGTH:  #As long as the size of the list is greater than MAX_LENGTH."
        removed_item = lst.pop()  #Do remove the last element
        print("Removed:", removed_item)  #Print the removed item."

def main():
    lst = []  #
    
    # "Take list input from the user."
    n = int(input("Enter number of elements in the list: "))
    for _ in range(n):
        value = input("Enter a value: ")
        lst.append(value)

    print("Original list:", lst)  # print the First List
    shorten(lst)  # Call to shorten function 
    print("Shortened list:", lst)  #Print the Final list 


if __name__ == '__main__':
    main()