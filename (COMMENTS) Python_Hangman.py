# This is the game hangman coded using python. This is a simple command line game allowing for the user to 
# input and output a visual of the current hangman alongside the word that is being guessed at every turn.
# The User wins if the word is guessed before running out of the 6 allowed tries. User looses if the
# correct word cannot be guessed within the allowed 6 tries.

####PYTHON NOTES:
##FUNCTIONS: are declared only by "def" and (): which is all thats needed to define a function.
##WHILE LOOPS: This is one of the two loop commands in python that is used to execute a set of
# statements as long as a condition is true. This requires relevant variables to be ready for use.
# Example: Print i as long as i is less than 6:
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# Within while loops, there are statements like break, continue, and else. The break statement is
# used to stop the loop even if the while condition is true.
# Example: Exit the loop when i is 3:
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# Continue statement is used to stop the current iteration, and continue with the next
# Example: Continue to the next iteration if i is 3:
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# Else statement is used to run a block of code once when the condition no longer is true.
# Example: Print a message once the condition is false:
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
##FOR LOOPS: Besides While loops, the other type of loop command is a "for loop" and is used for 
# iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator 
# method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#   Example
#   Print each fruit in a fruit list:
#       fruits = ["apple", "banana", "cherry"]
#       for x in fruits:
#           print(x)
#   This prints: apple banana cherry
# Similar to while loops, for loops also have statements like break, continue, and else.
##APPEND METHOD: The append() method appends an element to the end of the list.
# Example: Add an element to the fruits list:
#   fruits = ["apple", "banana", "cherry"]
#   fruits.append("orange")
#   print(fruits)
#This prints: ['apple', 'banana', 'cherry', 'orange']
##LIST COMPREHENSION: List comprehension offers a shorter syntax when you want to create a new list 
# based on the values of an existing list.
# Example:
#   Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
#   Without list comprehension you will have to write a for statement with a conditional test inside:
#       fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#       newlist = []
#       for x in fruits:
#           if "a" in x:
#               newlist.append(x)
#       print(newlist)
#   With list comprehension you can do all that with only one line of code:
#   Example
#       fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#       newlist = [x for x in fruits if "a" in x]
#       print(newlist)

  

## IMPORTS
## importing the 50 word list from the separate "Hangman_Words.py" file
## We want to randomly choose a word from this list so also importing the "random library"
import random
from Hangman_Words import List_Of_Words

##GET WORD FUNCTION
def get_word():
    ## The "word = random" part randomises the gotten word from the word list
    word = random.choice(List_Of_Words)
    ## The "return word" part returns the word in all upper case for the user to read
    return word.upper()

###PLAY FUNCTION 
## For the actual interactive game play this function "play". We create variables that update
## during each turn the user takes. "word" inside the play function displays the word during each turn.
def play(word):
    ## We need to represent unguessed letters as "_" and show the real letters as correct guesses are made.
    ## To do this we use "word_completion" string variable. This will be the same length as the chosen word.
    ## It will initially contain underscores.
    word_completion = "_" * len(word)
    ## Next we will initialized to false.
    guessed = False
    ## Now we create two lists. One that will hold the "letters" the user guessed...
    guessed_letters = []
    ## ...and one that will hold the "words" the user guessed
    guessed_words = []
    ## Last variable will be the number of tries. It corrisponds to the number of body parts
    ## left to be drawn on the hangman before the user looses or wins.
    tries = 6
    
    ## After initalizing the variables, lets "print" some initial output to help guide the user
    ## when the game starts.
    print("Ready? Start Playing!")
    ## "Print" the initial state of the hangman.
    print(display_hangman(tries))
    ## "Print" the initial state fo the word but in all underscores "____"
    print(word_completion)
    ## """"QUESTION: WHAT IS (((\N)))""""" ## "Print" a new line here.
    print("\n")
    
    ## The main chunk of our code is encompassed in this "WHILE LOOP" (see notes above) and
    ## this will run until ether the user wins or looses.
    while not guessed and tries > 0:
        ## Since each iteration the loop corrisponds to a turn by the user we will first prompt the
        ## user for a guess with this input as a guide and we will store the guess in a variable.
        ## Also make sure to cast this to upper case using "upper"
        guess = input("guess a letter or word: ").upper()
        ## Inside the loop we will have two possible conitional branches each base on different user
        ## input. This will include guessing a letter, guessing the word, or typing something other than a
        #  single letter or word the correct length. 
        # We will create this "if else" block (See notes). Guessing a letter would mean "guess" has a
        # length of 1 and contains only characters from the alphabet. So we will call "isalpha" on "guess"
        if len(guess) == 1 and guess.isalpha():
            # Lets start with what happens when guessing a letter. We will need another conditional
            # Block inside this if statement to check if the letter has already been guessed, is not
            # in the word, or is in the word. So if guess is in guessed letters, lets print this to prompt
            # The user to let them know the user has already guessed the letter and print the letter too.
            if guess in guessed_letters:
                print("You already guessed this letter", guess)
            ## Guessing a word would mean that the length of guess equals the length of the actual word
            #  and contains only letters. 
            # This will print to prompt the user that the guessed letter is not in the word.
            elif guess not in word:
                print(guess, "is not in the word.")
                # Here we will also decrement the number of tries by 1 since the user guessed wrong.
                tries -= 1
                # We will also append (see notes) guessed letters.
                guessed_letters.append(guess)
            # The only other possibility is if the user makes a correct guess so we will make an else
            # block and print a positive expression to prompt the user that they guessed correct.
            else:
               print("Good Job,", guess, "is in the word!")
               # Once again we will append guess to guessed letters.
               guessed_letters.append(guess)
               # Next we need to update our variable word completion to reveal to the user all occurences
               # of guessed. For this we will first convert word completion from a string to a list
               # so we are able to index into it and we will store this into a new variable called
               # word as list.
               word_as_list = list(word_completion)
               # Now we need to find all the indexes where guess occurs in the word so lets use a list 
               # comprehension (see notes). Here we are calling enumerate onward to get both the index i
               # and letter at the index for each iteration. We are pending i to this list if it's
               # corresponding letter equals guess.
               indices = [i for i, letter in enumerate(word) if letter ==guess]
               # Now we are going to use a simple "for loop" (see notes) over indices
               for index in indices:
                   # The for loop will be used to replace each underscore at index with guess.
                   word_as_list[index] = guess
               # Then lets update word completion with the new changes by calling empty string join
               # onwards as list to convert it back to a string.
               word_completion = "".join(word_as_list)
               # It is also a possibility that guess now completes the word so lets make an if statement
               # to check this. If underscore not in word completion, guessed equals true.
               if "_" not in word_completion:
                    guessed = True
        # Now lets do the conditional for guessing a word. Similar to guessing a word we need another 
        # conditional block inside of the if statement checking if the word has already been guessed and
        # is correct or is incorrect.
        elif len(guess) == len(word) and guess.isaplpha():
            # So if guessed is in guessed words, lets print this prompt to tell the user 
            # they already guessed the word.
            if guess in guessed_words:
                print("You already guessed the word", guess)
            # if guessed does not equal word, lets print this output to prompt 
            # the user that the guess is not in the word.
            elif guess != word:
                print(guess, "is not the word.")
                # Once again, lets decrement the number of tries by 1.
                tries -= 1
                # Once again, lets remember to append guess to guessed words.
                guessed_words.append(guess)
            # Then in this else statement, this is when the user correctly guessed the word.
            # We will set guessed to true and word completion to the full word.
            else:
                guessed = True
                word_completion = word
        # Then we will have and else statement that will catch everything else and we can print
        # "wrong" to alert the user that guess was wrong.
        else:
            print("Wrong")
        # after each guess is handled, we will print the current state of the hangman and the word.
        print(display_hangman(tries))
        # We will also print a new line to space out each turn. 
        print(word_completion)
        print("\n")
        # This finishes up our "while loop" from above.
    # After the while loop, lets check whether the user guessed the word correctly or ran out of
    # tries and lost. To do that lets check if guess is true and if so, print this output to prompt
    # the user that they won.
    if guessed:
        print("You Win!")
    # If not, print this output to prompt the user that they lost and reveal the correct word.
    else:
        print("You loose. The word was" + " " + word)

## These are the 7 visual stages of hangman. It is stored in a list within the function called
## "display hangman". The index of each stage corresponds to the number of tries the user has left.
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

# Finally we need this main function to put everything together.
def main():
    # Lets first get a word from get word.
    word = get_word()
    # Then lets pass this word to play. This is all we need here to run the game once but lets add
    # some code to give the user the option to play again.  
    play(word)
    # To do this, lets create a while loop to ask the user for input to prompt a redo of the game.
    # We will call upper on the input and check if it is equal to Y.
    while input("Play Again? (Y/N)").upper() == "Y":
        # Then inside we will call the same two functions we did before. This way our program will
        # continue for as long as the user presses yes to play again.
        word = get_word()
        play(word)
# Lastly we will add this fragment of code to ensure this program will run by running this script on
# the command line/command prompt.
if __name__ == "__main__":
    main()