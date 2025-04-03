#Print 10 random numbers in the range 1 to 100.

import random

N_NUMBERS: int = 10  # "Generate 10 numbers."
MIN_VALUE: int = 1    # Minimum value 1
MAX_VALUE: int = 100  # Maximum value 100

def main():
    # "Generate 10 random numbers and print them in a single line."
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

    print()  # Newline for better formatting

if __name__ == '__main__':
    main()