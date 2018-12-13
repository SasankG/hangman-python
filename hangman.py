import random

# Word Array
words = ["cat", "bird", "mammal", "dinosaur", "dog", "computer"]
lives = 10

# Random Word
def random_word():
    rword = random.choice(words)
    return rword

# Check for letters and generate blank string
def letter_check(word, guess, attempt):
    blanks = ""
    match = 0
    for letter in word:
        if letter in guess:
            blanks += letter
        elif letter == attempt:
            match += 1
        else:
            blanks += " _ "
    if match == 1:
        print("Yup, " + attempt + " was in the word!")
    else:
        print("Keep guessing!")
    return blanks 

# Main Game
def game():
    print(" ")
    print("Welcome to Hangman! A random word was generated, try to guess it!")
    word = random_word()
    guess = []
    correct = False
    introword = ""
    while not correct:
        
        #User Attempt
        mytry = input("Guess a letter ")
        
        # If the letter was already guessed
        if mytry in guess:
            print(mytry + " was already guessed")
        
        # If they guess the whole word
        elif len(mytry) == len(word):
            # If the whole word guessed is correct
            if guess == word:
                correct = True
            else:
                print("Sorry try again")
        
        # If they guess a single letter
        elif len(mytry) == 1:
            # Add their guess to the guess array
            guess.append(mytry)
            # Get result back from the letter check
            result = letter_check(word, guess, mytry)
            if result == word:
                correct = True
            else:
                # Print out the word in blanks
                print(result)
        # If invalid guess
        else:
            print("Enter again")
    
    print("Correct you won! the word was " + word + "!")

game()