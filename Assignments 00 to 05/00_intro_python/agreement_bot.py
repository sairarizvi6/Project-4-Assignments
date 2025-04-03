#Write a program which asks the user what their favorite animal is, 
#and then always responds with "My favorite animal is also ___!" 
# (the blank should be filled in with the user-inputted animal, of course).


def main(fav_animal: str) -> str:
    return f"My favorite animal is also {fav_animal}!"

user_input = input("What's your favorite animal? ")
result = main(user_input)
print(result)



