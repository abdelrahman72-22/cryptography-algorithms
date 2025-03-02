
from itertools import permutations
import string

# English letter frequency (approximate order)
FREQUENCY_ORDER = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

# Function to decrypt text using a given key mapping
def decrypt(text, key_map):
    return "".join(key_map.get(char, char) for char in text)

# Brute-force function to try different key mappings
def brute_force_monoalphabetic(ciphertext):
    ciphertext = ciphertext.upper()
    unique_chars = sorted(set(ciphertext) & set(string.ascii_uppercase))
    
    # Generate possible mappings using letter frequency analysis
    for perm in permutations(FREQUENCY_ORDER[:len(unique_chars)], len(unique_chars)):
        key_map = dict(zip(unique_chars, perm))
        decrypted_text = decrypt(ciphertext, key_map)
        print(f"Trying key: {key_map}\nDecrypted text: {decrypted_text}\n")

# User interaction
if __name__ == "__main__":
    cipher_text = input("Enter the encrypted text: ")
    brute_force_monoalphabetic(cipher_text)
