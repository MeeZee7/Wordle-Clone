import random

def load_dictionary(file):
    with open(file) as f:
        words = [line.strip() for line in f]  # Call strip() correctly

    return words    

def is_valid(guess, guesses):
    return len(guess) == 5 and guess in guesses

def evaluate(guess, word):
    result = ""

    for i in range(5):
        if guess[i] == word[i]:
            result += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                result += "\033[33m" + guess[i]
            else:
                result += "\033[0m" + guess[i]

    return result + "\033[0m"

def wordle(guesses, answers):
    print("Welcome to Wordle! You have 6 attempts to guess a 5-letter word.")
    print("A letter in its correct position is colored \"Green\".")
    print("A letter present in the word is colored \"Yellow\".")
    secret_word = random.choice(answers).lower()

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input("Enter #" + str(attempts) + ": ").lower()

        if guess == secret_word:
            print(f"Congratulations! You have guessed the word correctly: {secret_word}")
            break

        if not is_valid(guess, guesses):
            print("Invalid attempt. Please enter a valid word again.")
            continue

        feedback = evaluate(guess, secret_word)
        print(feedback)

        attempts += 1

    if attempts > max_attempts:
        print(f"Game Over. The secret word was {secret_word}")

guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

wordle(guesses, answers)



             
 
      

#\033[32m-->green
#\033[33m-->yellow
#\033[0m-->default