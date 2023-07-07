import random

def guess_number():
    secret_number = random.randint(1, 50)
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print(secret_number)
            print("Too low! Try a different number.")
        elif guess > secret_number:
            print(secret_number)
            print("Too high! Try a different number.")
        else:
            print(secret_number)
            print("You won!!")
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

if __name__ == '__main__':
    guess_number()