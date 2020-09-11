# Problem Set 2, hangman.py

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # Make a set of letters in secret word
    secret_letters = set()
    for s in secret_word:
        if s not in secret_letters:
            secret_letters.add(s)

    # Iterate through guessed letters list, removing matches from secret word set
    for g in letters_guessed:
        if g in secret_letters:
            secret_letters.remove(g)

    # If secret letter set is empty, all letters were matched, so return true. Else, return false.
    if len(secret_letters) == 0:
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # Make a set from letters_guessed
    guess_set = set(letters_guessed)
    
    # Iterate through secret word, creating a string with letters for correct guesses and blanks for missed letters
    # TODO: Add spaces between blanks and characters (use a counter)
    guess_array = []
    for s in secret_word:
        if s in guess_set:
            guess_array.append(s)
        else:
            guess_array.append('_')
    guess_string = ''.join(guess_array)

    return guess_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
   # Make a string of all ascii alphabets
    alphastring = string.ascii_lowercase

    # Delete guessed characters from alphabet string and return the resulting list of available letters
    for l in letters_guessed:
        alphastring = alphastring.replace(l,'')

    return alphastring
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Initialize variables
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    # Print game start message
    print ("Welcome to the game Hangman!\n")
    print("I am thinking of a word that is",len(secret_word),"letters long.\n")
    print("-----------------")

    while guesses_remaining > 0:
        available_letters_string = get_available_letters(letters_guessed)
        available_letters_set = set(available_letters_string)
        print("You have",guesses_remaining,"left.\n")
        print("Available letters:",available_letters_string)

        # ------ TODO: Refactor this into a separate function -------- #

        # Get and validate user input
        invalid_input = False
        user_guess = input("Please guess a letter: ")
        if not str.isalpha(user_guess):
            print("Invalid character detected.") 
            invalid_input = True
        elif user_guess not in available_letters_set:
            print("Letter already guessed.")
            invalid_input = True

        # Warning for invalid user input
        if invalid_input:
            print("Please guess one alphabetic character from the list of available characters (no numbers, symbols, or previously-guessed letters).")

            # If user has warnings remaining, take one away
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("You have," warnings_remaining, "warnings left.")

            # If three invalid user inputs, user loses a guess.
            if warnings_remaining == 0:
                print("You have no warnings left. Penalty: Lose a guess.")
                guesses_remaining -= 1

        # If user input is valid, remove the guess from the string and set of available letters and proceed
        else:
            available_letters_string.replace(user_guess, '')
            available_letters_set.remove(user_guess)
            check_secret_word(user_guess, secret_word))

        # ----- End of user input validation/warning/penalty code ----- #

def validate_user_input(user_guess):
    # User input validation
    pass

def check_secret_word(user_guess, secret_word):
    '''
    Implement game rules.
    1. If user guesses a letter (not previously guessed) in the secret word, lose no guesses.
    2. If user guesses a consonant (not previously guessed) not in the secret word, lose one guess.
    3. If user guesses a vowel (not previously guessed) not in the secret word, lose two guesses.

    Print informational message including:
    Number of guesses left
    Available letters
    Whether the user guessed correctly or incorrectly
    Word with gaps (blanks for letters not yet guessed)
    '''
    pass


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # Load the list of words into the variable wordlist
    wordlist = load_words()

    # Choose a random word, and ensure that it is all lowercase
    secret_word = str.lower(choose_word(wordlist))

    hangman(secret_word)
