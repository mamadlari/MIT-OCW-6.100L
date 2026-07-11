# MIT 6.100L : Problem Set 3

This repository contains the complete implementation for **Problem Set 3**, which focuses on data structures (specifically Python dictionaries), string manipulation, character frequency maps, and building an interactive game loop (a Scrabble-like Word Game with wildcard capabilities).

---

## Project Structure

* **`ps3.py`:** The main implementation file containing the logic for score calculation, hand updates, word validation, wildcard mechanics, and the interactive gameplay loop.
* **`test_ps3.py`:** The student testing suite containing unit tests to validate individual functions like `get_word_score`, `update_hand`, and `is_valid_word`.
* **`words.txt`:** A plain text file acting as the dictionary database containing a list of over 83,000 valid lowercase English words.

---

## Detailed Components

### Part 1: Scoring and Hand Mechanics

* **Word Score Calculation (`get_word_score`)**: Computes points based on individual letter values (similar to Scrabble). The score is calculated by multiplying the sum of the letter frequencies by the length of the word, adding an additional length bonus if all characters in the initial hand are successfully used.
* **Hand Manipulation (`update_hand`)**: Safely updates a player's hand after a word is played. It creates a deep copy of the hand dictionary to protect it from unexpected mutation, reducing the frequency values of utilized letters or removing them entirely.

### Part 2: Word Validation & Wildcards

* **Validation Logic (`is_valid_word`)**: Ensures that a user-submitted word is entirely constructible using the current hand frequencies and verifies its existence within the `words.txt` dictionary array.
* **Wildcard Integration (`*`)**: Exactly one wildcard character (`*`) is introduced per dealt hand. It represents any vowel (`a`, `e`, `i`, `o`, `u`). The validation algorithm seamlessly branches out to verify if any valid English vowel satisfies the dictionary constraint when a wildcard is used.

### Part 3: Interactive Gameplay Loop

* **Playing a Single Hand (`play_hand`)**: Governs the interactive text interface for a single round. It displays the current hand, prompts the user for inputs, computes intermediate scores, and tracks remaining available letters until the hand is depleted or the user inputs `!!` to quit.
* **Managing the Entire Game (`play_game`)**: Orchestrates series of consecutive hands. It features advanced configuration options allowing players to choose to substitute an undesirable letter before starting, or selectively replay a finished hand to maximize their total cumulative game score.

---

## Important Constraints & Style Guidelines

* **Immutable Frequency Access**: When constructing or manipulating frequency distribution maps (dictionaries), deep copies must be performed to avoid inadvertent side effects when calling down-stack validation routines.
* **Case-Insensitive Constraints**: All inputs must be converted seamlessly to lowercase syntax, ensuring robust comparison routines against the standard lowercased lookup dictionary (`words.txt`).
* **Wildcard Constraints**: The wildcard `*` only assumes vowel values. It cannot be substituted for consonants during the lookup phase, and it awards 0 point values on its own.

---

## Testing

Run the local unit test suite to ensure that your helper functions comply with the formal parameter expectations and corner cases:

```bash
python test_ps3.py

```

---
