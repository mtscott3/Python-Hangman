# This is the game hangman coded using python. This is a simple command line game allowing for the user to 
# input and output a visual of the current hangman alongside the word that is being guessed at every turn.
# The User wins if the word is guessed before running out of the 6 allowed tries. User looses if the
# correct word cannot be guessed within the allowed 6 tries.

##IMPORTS
import random
from Hangman_Words import List_Of_Words


##GET WORD FUNCTION
def get_word():
    word = random.choice(List_Of_Words)
    return word.upper()

##PLAY FUNCTION 
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Ready? Start Playing!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
               print("Good Job,", guess, "is in the word!")
               guessed_letters.append(guess)
               word_as_list = list(word_completion)
               indices = [i for i, letter in enumerate(word) if letter ==guess]
               for index in indices:
                   word_as_list[index] = guess
               word_completion = "".join(word_as_list)
               if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isaplpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Wrong")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("You Win!")
    else:
        print("You loose. The word was" + " " + word)


def display_hangman(tries):
  stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
  return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()