# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    corrent_letters = 0
    for letter in secret_word:
        if letter in letters_guessed:
            corrent_letters += 1
    if len(secret_word) == corrent_letters:
        return True
    else:
        return False


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    words_guessed = ""
    for letter in secret_word:
        star = True
        if letter in letters_guessed:
            words_guessed += letter
            star = False
        if star == True:
            words_guessed += "*"
    return words_guessed


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ""
    for letter in string.ascii_lowercase:
        available = True
        if letter in letters_guessed:
            available = False
        if available == True:
            available_letters += letter
    return available_letters


def _input():
    letter = input("Please guess a letter: ")
    if len(letter) == 1:
        if letter.isalpha() == True:
            letter = letter.lower()
            return letter
        if letter == "!":
            return letter
    return False


def repetitive(letters_guessed, letter):
    for char in letters_guessed:
        if letter == char:
            return True
    return False


def In_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    return False


def consonants(letter):
    vowels_letter = ("e", "a", "u", "i", "o")
    if letter in vowels_letter:
        return False
    else:
        return True


def _help(secret_word, available_letters):
    choose_from = ""
    for letter in available_letters:
        if letter in secret_word:
            choose_from += letter
    new = random.randint(0, len(choose_from) - 1)
    revealed_letter = choose_from[new]
    return revealed_letter


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 10
    letters_guessed = ""
    print("Welcome to Hangman!")
    print(
        "I am thinking of a word that is ", len(secret_word), "letters long."
    )
    while guesses != 0:
        print("--------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        letter = _input()
        if letter == False:
            print(
                "Oops! That is not a valid letter. Please input a letter from the alphabet :",
                get_word_progress(secret_word, letters_guessed),
            )
        else:
            if with_help == False and letter == "!":
                print(
                    "Oops! That is not a valid letter.Becuase it isn't a with help game:",
                    get_word_progress(secret_word, letters_guessed),
                )
            elif letter == "!":
                if guesses >= 3:
                    revealed_letter = _help(
                        secret_word, get_available_letters(letters_guessed)
                    )
                    letters_guessed += revealed_letter
                    print("Letter revealed :", revealed_letter)
                    print(get_word_progress(secret_word, letters_guessed))
                    guesses -= 3
                else:
                    print(
                        "Oops! Not enough guesses left :",
                        get_word_progress(secret_word, letters_guessed),
                    )
            elif repetitive(letters_guessed, letter):
                print(
                    "Oops! You've already guessed that letter :",
                    get_word_progress(secret_word, letters_guessed),
                )
            else:
                if In_secret_word(letter, secret_word):
                    letters_guessed += letter
                    print(
                        "Good guess :",
                        get_word_progress(secret_word, letters_guessed),
                    )
                else:
                    print(
                        "Oops! That letter is not in my word:",
                        get_word_progress(secret_word, letters_guessed),
                    )
                    if consonants(letter):
                        guesses -= 1
                    else:
                        guesses -= 2


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    secret_word = "tact"
    with_help = False
    hangman(secret_word, with_help)
