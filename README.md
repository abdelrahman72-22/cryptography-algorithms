# cryptography-algorithms
This repository contains implementations of various classical cryptographic algorithms, including:

Caesar Cipher

Vigenère Cipher

Playfair Cipher

Brute-force Attack on Monoalphabetic Ciphers

1. Caesar Cipher

The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

Encryption Formula:

C = (P + K) mod 26

Where:

C = Ciphertext letter

P = Plaintext letter (converted to index: A=0, B=1, ... Z=25)

K = Shift key

Decryption Formula:

P = (C - K) mod 26

Example:

Plaintext: HELLO

Key: 3

Ciphertext: KHOOR

2. Vigenère Cipher

The Vigenère cipher is a polyalphabetic substitution cipher that uses a repeating key to shift each letter.

Encryption Formula:

C[i] = (P[i] + K[i]) mod 26

Decryption Formula:

P[i] = (C[i] - K[i]) mod 26

Where:

P[i] and C[i] are letters of the plaintext and ciphertext.

K[i] is the corresponding letter from the repeating keyword, converted to numerical form.

Example:

Plaintext: ATTACK

Key: LEMON

Ciphertext: LXFOPV

3. Playfair Cipher

The Playfair cipher is a digraph substitution cipher that encrypts pairs of letters using a 5x5 key square.

Steps:

Create a 5x5 matrix using a keyword, removing duplicate letters.

Split plaintext into digraphs (pairs of two letters).

Apply Playfair encryption rules:

Same row: Shift right.

Same column: Shift down.

Forming a rectangle: Swap corners.

Example:

Keyword: MONARCHY

Plaintext: HELLO → HE LL OX

Ciphertext: KF RZ SY

4. Brute-force Attack on Monoalphabetic Ciphers

Monoalphabetic ciphers use a fixed substitution where each letter is mapped to another letter.

Brute-force Approach:

Try all 26 possible shifts (for Caesar cipher) or other systematic substitutions.

Check for meaningful words in English.

Use frequency analysis to identify common letters (e.g., E, T, A, O, I, N).
