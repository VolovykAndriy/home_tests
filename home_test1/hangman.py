# Problem Set 2, hangman.py
# Name: Volovyk Andriy
# Collaborators:
# Time spent:

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


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
        if i in letters_guessed:
            continue
        else:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    players_word = str()
    for i in secret_word:
        if i in letters_guessed:
            players_word += i
        else:
            players_word += "_ "
    return players_word


def get_available_letters(letters_guessed):
    available_letters = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in available_letters:
            available_letters.remove(i)
    return "".join(available_letters)


def check_input(letter, warnings, letters_guessed):
    if not letter.isalpha() or len(letter) != 1:
        warnings -= 1
        if warnings < 0:
            print(
                "Oops! That is not a valid letter."
                "You have no warnings left so you lose one guess: "
                f"{get_guessed_word(secret_word, letters_guessed)}"
            )
        else:
            print(
                "Oops! That is not a valid letter."
                f"You have {warnings} warnings left: "
                f"{get_guessed_word(secret_word, letters_guessed)}"
            )
        return True
    elif letter.isalpha() and letter in letters_guessed:
        if warnings < 0:
            print(
                "Oops! You've already guessed that letter."
                "You have no warnings left so you lose one guess: "
                f"{get_guessed_word(secret_word, letters_guessed)}"
            )
        else:
            warnings -= 1
            print(
                "Oops! You've already guessed that letter."
                f"You have {warnings} warnings left:\n"
                f"{get_guessed_word(secret_word, letters_guessed)}"
            )
        return True
    return False


def hangman(secret_word):
    guesses = 6
    warnings = 3
    letters_guessed = list()
    print(
        "Welcome to the game Hangman!\n"
        f"I am thinking of a word that is {len(secret_word)} letters long\n"
        "-------------"
    )
    while True:
        if guesses <= 0:
            guesses = 0
        print(
            f"You have {guesses} guesses left\n"
            f"Available letters: {get_available_letters(letters_guessed)}"
        )
        if is_word_guessed(secret_word, letters_guessed):
            print(
                "Congratulations, you won!\n"
                "Your total score for this game is:"
                f"{len(set(secret_word))*guesses}"
            )
            break
        elif not guesses:
            print(
                "GAME OVER!\n"
                "Try your luck in the next game.\n"
                f"Your word was {secret_word}"
            )
            break
        else:
            while True:
                letter = input("Please guess a letter: ").lower()
                if not check_input(letter, warnings, letters_guessed):
                    break
                else:
                    warnings -= 1
                    if warnings < 0:
                        guesses -= 1
                    continue
            letters_guessed.append(letter)
            if letters_guessed[-1] in secret_word:
                print(
                    f"Good guess: {get_guessed_word(secret_word, letters_guessed)}"
                )
            else:
                print(
                    "Oops! That letter is not in my word: "
                    f"{get_guessed_word(secret_word, letters_guessed)}"
                )
                if letter in "bcdfghjklmnpqrstvwxyz":
                    guesses -= 1
                elif letter in "aeiou":
                    guesses -= 2
            print("-----------")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
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
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
