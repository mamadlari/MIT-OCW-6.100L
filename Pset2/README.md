# MIT 6.100L : Problem Set 2

This repository contains the complete implementation for **Problem Set 2**, which focuses on basic Python types, string manipulation, loops, control flow, and building an interactive command-line game (**Hangman** and **Hangman with Hints**).

---

## Project Structure

* **`hangman.py`:** The main implementation file containing the core game logic, user input processing, string formatting routines, and the hint-matching algorithm.
* **`test_ps2.py`:** The student testing suite containing unit tests to validate individual helper functions.
* **`words.txt`:** A text file containing a list of over 55,000 valid lowercase English words used as the game's secret word database.

---

## Detailed Components

### Part 1: Core Helper Functions

* **Tracking Guesses (`is_word_guessed`)**: A function that checks whether all letters of the secret word have been successfully uncovered by comparing the list of guessed letters against the target string.
* **Formatting the Display (`get_guessed_word`)**: Dynamically constructs a string representing the current state of the game board. Letters that haven't been guessed yet are displayed as underscores followed by a space (`_ `) to maintain clear readability for the player.
* **Available Letters (`get_available_letters`)**: Computes and returns a string of all remaining lowercase English letters that the user has not yet guessed, providing crucial feedback during gameplay.

### Part 2: Interactive Hangman Loop

* **Game Initialization**: Selects a random secret word from the text database and provides the user with 8 initial guesses and 3 warnings.
* **Input Validation & Warning System (`hangman`)**: Tracks user input dynamically. If a user enters a non-alphabetical character or a letter they have already guessed, they lose a warning. If they run out of warnings, they lose an entire guess instead.
* **Penalty Rules**: Guesses are managed strictly based on character type. An incorrect consonant guess costs **1 guess**, while an incorrect vowel guess costs **2 guesses**.

### Part 3: Hangman with Hints (Advanced Pattern Matching)

* **Gap Matching (`match_with_gaps`)**: Implements an algorithm that takes the current partially revealed hidden word (e.g., `a _ _ l _`) and matches it against any candidate word from the dictionary. It accounts for length constraints and ensures that revealed letters are not repeated in hidden slots.
* **Show Possible Matches (`show_possible_matches`)**: Iterates through the entire word list using the gap-matching logic to print out all valid English words that could fit the current board state.
* **Hint Triggering (`hangman_with_hints`)**: Integrates the hint logic into the core loop. Players can type the asterisk symbol (`*`) as their input to instantly view a list of all potential dictionary matches to help them complete the word.

---

## Important Constraints & Style Guidelines

* **Case Insensitivity**: The game must seamlessly convert all user inputs to lowercase syntax to maintain clean comparison matching against the lowercase word bank.
* **Score Calculation**: At the end of a winning game, the total score is computed using the formula:

$$\text{Total Score} = \text{Guesses Remaining} \times \text{Number of Unique Letters in Secret Word}$$


* **String Immutability**: Since Python strings are immutable, all display updates must be efficiently built using string concatenation or list-joining techniques.

---

## Testing

Run the local unit test script to verify that your core helper functions behave as expected across various edge cases before testing the interactive loops:

```bash
python test_ps2.py

```
