# 1. Pick a secret treasure (replace "secret_treasure" with your choice)
treasure = "3"

# 2. Welcome message
print("Welcome to the Treasure Hunt!")

# 3. Loop for guesses (replace the number with how many guesses you want to allow)
for guess_count in range(3):
 # 4. Ask the player for a guess and store it in the variable 'guess'
    guess = input("Take a guess: ")

  # 5. Check if the guess is correct using a conditional statement (if...else)
    if guess == treasure:
        # Tell the player they won!
        print("Congratulations! You found the treasure!")
        # Exit the loop (no more guesses needed)
        break  # This is the 'break' statement
    else:
        # Tell the player they guessed wrong and offer another try
        print("Nope, try again!")

# Outside the loop, tell the player if they didn't guess it in time
print("Out of guesses! The treasure was", treasure)