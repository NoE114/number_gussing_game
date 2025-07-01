import random

smallest_num = 1
largest_num = 100
answer = random.randint(smallest_num, largest_num)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"Guess a number between {smallest_num} and {largest_num}.")

while is_running:
    guess = input("Enter your guess (or type 'exit' to quit): ")

    if guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break

    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue

    guesses += 1

    if guess < smallest_num or guess > largest_num:
        print(f"Your guess is out of bounds! Please guess a number between {smallest_num} and {largest_num}.")
    elif guess < answer:
        print("Too low! Try again.")
    elif guess > answer:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {answer} in {guesses} tries.")
        is_running = False

