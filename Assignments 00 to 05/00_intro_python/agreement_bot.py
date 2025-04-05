#Write a program which asks the user what their favorite animal is, 
#and then always responds with "My favorite animal is also ___!" 
# (the blank should be filled in with the user-inputted animal, of course).


def main():

    animal = input("\033[1;3m What's your favorite animal? \033[0m")


    print(f"My favorite animal is also {animal}!")


if __name__ == '__main__':
    main()



