import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Specify the range
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    # Generate a random number
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    print(f"I have chosen a number between {lower_bound} and {upper_bound}. Can you guess it?")
    
    while True:
        # Get user input
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check the guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
            break

# Start the game
if __name__ == "__main__":
    number_guessing_game()

