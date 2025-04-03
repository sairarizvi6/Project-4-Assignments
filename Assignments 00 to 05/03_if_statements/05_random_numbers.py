import random  #to import the Random module 

def main():
    # Generate 10 random numbers and print them space-separated."
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print(*random_numbers)

#This is necessary to run the program.
if __name__ == '__main__':
    main()