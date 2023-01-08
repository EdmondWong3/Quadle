import random
import sys

lives = 7
letter_1_found = False; letter_2_found = False; letter_3_found = False; letter_4_found = False
tracker = []

def random_word(): # Reads the file and picks a random 4-letter word.
    file = open("words.txt", "r")
    list_of_words = file.readlines()
    word = random.choice(list_of_words)
    return word


def word_to_list(): # Puts each letter of the chosen word into a list with its own individual index.
    list_of_letters = []
    word = random_word()
    for letter in word:
        list_of_letters.append(letter)
    del list_of_letters[-1]
    return list_of_letters


def guess_letter(): # Have the player guess a single letter.
    while True:
        letter = input("Guess Letter > ").lower()
        if len(letter) != 1 or letter.isalpha() is False:
            print("Please enter a single lettter.")
        else:
            return letter


def check_letter_exist(guess, word): # Checks to see whether the guessed letter is in the word and determines an appropriate response.
    global letter_1_found, letter_2_found, letter_3_found, letter_4_found, lives
    if guess == word[0]:
        letter_1_found = True
    if guess == word[1]:
        letter_2_found = True
    if guess == word[2]:
        letter_3_found = True
    if guess == word[3]:
        letter_4_found = True
    if guess != word[0] and guess != word[1] and guess != word[2] and guess != word[3]:
        lives -= 1
    return letter_1_found, letter_2_found, letter_3_found, letter_4_found, lives


def status_update(word): # Updates the status of the word when a letter of the word is discovered.
    update = []
    if letter_1_found is True:
        update.insert(0, word[0])
    else:
        update.insert(0, "?")
    if letter_2_found is True:
        update.insert(1, word[1])
    else:
        update.insert(1, "?")
    if letter_3_found is True:
        update.insert(2, word[2])
    else:
        update.insert(2, "?")
    if letter_4_found is True:
        update.insert(3, word[3])
    else:
        update.insert(3, "?")
    return update
    

def letter_tracker(guess): # Makes the player's life easier by keeping track of the letters they used.
    global tracker
    tracker.append(guess)
    return tracker


def victory_defeat_check(word): # Checks whether the player has achieved victory or has been defeated.
    if lives > 0:
        sys.exit("\n✧˖° Congrats, you won! ✧˖°\n")
    else:
        string = ""
        for letter in word:
            string += letter
        sys.exit(f"\nYou lost. The word is '{string}'\n")


def play_quadle():
    print("""
    Welcome to Quadle (Inspired by Wheel of Fortune and New York Times' Wordle)
    
    Rules:
        1. In order to win, players have to guess the 4-letter English word.
        2. Players' guesses have be letters and not the word itself.
        3. Players have five lives. Every failure to guess a letter contained in the word will result in the loss of a life.
        4. If your lives hit zero, you lose. 
    """)

    word = word_to_list() # Choose a random word out of the 333 available words.
    print(f"Word: ['?', '?', '?', '?']    Letters Tried: [ ]    Lives: 7")

    while (letter_1_found is False or letter_2_found is False or letter_3_found is False or letter_4_found is False) and lives > 0: # For the game to end, either all 4 letters have to be guessed correctly or the number of lives drops to 0.
        guess = guess_letter() # Player guesses a letter.
        check_letter_exist(guess, word) # Checks to see whether the letter guessed by the player is in the word or not.
        tracker = letter_tracker(guess) # Lets the player know what letters they have tried so far.
        update = status_update(word) # Updates the visual representation of the word.
        print(f"Word: {update}    Letters Tried: {tracker}    Lives: {lives}")
    
    victory_defeat_check(word) # Checks to see whether the player has won or lost.


if __name__ == "__main__":
    play_quadle()