import random
def Guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
Guessing_game()