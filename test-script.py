import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Number of guesses allowed
guesses = 5

while guesses > 0:
  # Get user's guess
  try:
    guess = int(input("Guess a number between 1 and 100 (you have " + str(guesses) + " guesses left): "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue

  guesses -= 1  # Decrement remaining guesses

  # Check the guess
  if guess == secret_number:
    print("Congratulations! You guessed the number in", 5 - guesses, "guesses.")
    break
  elif guess < secret_number:
    print("Your guess is too low.")
  else:
    print("Your guess is too high.")

if guesses == 0:
  print("You ran out of guesses. The secret number was", secret_number)
