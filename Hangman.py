# A basic Hangman game in Python

import random

# Possible words to be guessed
words = ["HOSPITAL", "DOCTOR", "HOUSE", "TOWN", "VILLAGE", "AUTOMOTIVE", "MERCEDES", "DOG", "BATTERY"]
word = random.choice(words)

number_guesses = round(len(word) * 1.5)

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

blanked_word = ""
for _ in range(0, len(word)):
    blanked_word += "_ "
blanked_list = blanked_word.split()
letters_guessed = ""
index_list = ""

print("Hangman Game in Python")


def game():
    # recursive function that runs the game

    global blanked_list
    global number_guesses
    global letters_guessed
    global index_list

    # Print empty and already guessed fields
    for i in blanked_list:
        print(i, end=" ")

    # Ask the user for a new letter
    new_letter = input("\nEnter the letter you want to try: ").upper()

    # Check if new letter has already been guessed
    if new_letter in blanked_list:
        print("Letter already used! Try again.")
        game()
        return

    # If new letter is part of to be guessed word and only occurs once, save it in blanked_list
    if word.find(new_letter) >= 0 and word.count(new_letter) == 1:
        index_in_word = word.index(new_letter)
        blanked_list[index_in_word] = new_letter

    # If new letter is part of to be guessed word and occurs multiple times, save it in blanked_list
    elif word.count(new_letter) > 1:
        for letter in range(0, len(word)):
            if word[letter] == new_letter:
                index_list += str(letter)
        for i in index_list:
            blanked_list[int(i)] = new_letter

    # If new letter is NOT part of to be guessed word
    else:

        if new_letter in letters_guessed:
            print("Letter already used! Try again.")
            game()
            return
        letters_guessed += new_letter
        print("Letter not found!")
        number_guesses -= 1
        if len(hangman_pics) < number_guesses:
            print(hangman_pics[0])
        else:
            print(hangman_pics[-number_guesses])
            if number_guesses == 1:
                print("Game Over :(")
                return

    if "_" not in blanked_list:
        print("Congratulations, you won!")

    game()


game()








