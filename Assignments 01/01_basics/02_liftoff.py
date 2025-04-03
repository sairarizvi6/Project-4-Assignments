#Write a program that prints out the calls for a spaceship that is about to launch.
# Countdown from 10 to 1 and then output Liftoff!

def main():
    # "Loop to count from 10 to 1."
    for i in range(10, 0, -1):  # "Reverse countdown from 10 to 1."
        print(i, end=" ")  # "Print in a single line."
    
    #"Print 'Liftoff!' when the countdown is over."
    print("Liftoff!")

# "Call the main function."
if __name__ == '__main__':
    main()