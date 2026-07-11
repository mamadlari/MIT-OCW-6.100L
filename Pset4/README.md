# MIT 6.100L : Problem Set 4

This repository contains the complete implementation for **Problem Set 4**, which covers recursive data structures (Binary Trees and Heaps) and Object-Oriented Programming (OOP) applied to cryptography (One-Time Pad Encryption).

---

## Project Structure

* **`ps4a.py` (Part A):** Contains recursive algorithms for calculating binary tree height and validating heap properties.
* **`ps4b.py` (Part B):** Contains the object-oriented design and class hierarchy (`Message`, `PlaintextMessage`, `EncryptedMessage`) for One-Time Pad encryption and decryption.
* **`ps4c.py` (Part C):** Applies the classes built in Part B to decrypt text using a list of potential pads and decodes an encrypted story.
* **Testing Suites:** * `test_ps4a_student.py` (Validates Part A functionality)
* `test_ps4bc_student.py` (Validates Parts B and C functionality)



---

## Detailed Components

### Part A: Trees and Heaps

* **Tree Height (`find_tree_height`)**: A strictly recursive function that calculates the maximum depth of a binary tree (the number of edges between the root and the furthest leaf node). Non-recursive implementations are invalid.
* **Heap Evaluation (`is_heap`)**: A recursive function that determines whether a tree qualifies as a Max-Heap or a Min-Heap based on a modular comparator function (`compare_func`).

### Part B: One-Time Pad Encryption (OOP & Inheritance)

Implements a secure text encryption technique by shifting characters within the ASCII range of **32 to 126** (wrapping around using modulo logic when necessary).

1. **`Message` (Parent Class)**: Implements base properties shared by all messages, such as initializing text, character shifting (`shift_char`), and applying a list of shifts (`apply_pad`).
2. **`PlaintextMessage` (Child Class)**: Extends `Message` to handle unencrypted text. It manages pad generation within the integer range **[0, 110)**, updates pads securely, and exposes the resulting ciphertext.
3. **`EncryptedMessage` (Child Class)**: Extends `Message` to handle ciphertexts. It implements `decrypt_message` by applying the negative values of the encryption pad to reverse the shifts.

### Part C: Ciphertext Decoding

* **Pad Evaluation (`decrypt_message_try_pads`)**: Takes a ciphertext and tests a list of possible one-time pads. It splits decrypted text by spaces and utilizes `is_word` to check for valid English words, identifying the correct pad by maximizing the valid word count. In the case of a tie, the last matching pad is chosen.
* **Story Reconstructon (`decode_story`)**: Automatically extracts an encrypted story string and a set of intercepted pads to decrypt and print Bob's hidden message to Alice.

---

## Important Constraints & Style Guidelines

* **No Direct Attribute Access**: In accordance with the MIT Style Guide, do not directly access or modify class attributes from external functions (e.g., inside Part C). Always use explicit **getter** and **setter** methods to maintain encapsulation.
* **Immutability Protection**: When dealing with mutable objects like lists (e.g., the encryption pad), always store and return a **copy** of the list to prevent external mutation errors.
* **Proper Inheritance**: The child classes (`PlaintextMessage` and `EncryptedMessage`) must correctly invoke the parent class constructor using `super().__init__(...)` to avoid code duplication.

---

## Testing

Run the following test scripts in your terminal to verify that your implementation passes all local test cases:

```bash
python test_ps4a_student.py
python test_ps4bc_student.py

```