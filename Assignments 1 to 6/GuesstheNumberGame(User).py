
import random
secret_number = random.randint(1, 10)
print("The computer has thought of a secret number! 🧠 Now, try to guess it! 🔢")
while True:
    user_guess = int(input("Enter your guess (1-10): "))
    if user_guess == secret_number:
        print("Congratulations! 🎉 You Got it Right! ✅")
        break
    elif user_guess > secret_number:
        print("Think smaller! 📉")
    else:
        print("Think bigger! 📈")