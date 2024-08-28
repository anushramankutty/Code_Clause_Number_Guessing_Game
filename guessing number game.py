import random

def guess_the_number_game():
    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    guess = None
    attempts = 0

    # Loop until the correct guess is made
    while guess != number_to_guess:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# Start the game
guess_the_number_game()
