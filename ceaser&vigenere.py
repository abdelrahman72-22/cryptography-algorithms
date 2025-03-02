
import string

def caesar_cipher(text, shift, encrypt=True):
    alphabet = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
    shift = shift if encrypt else -shift  # Reverse shift for decryption
    result = ""

    text = text.lower()  # Convert everything to lowercase

    for char in text:
        if char in alphabet:  # Process only alphabetic characters
            new_index = (alphabet.index(char) + shift) % 26
            result += alphabet[new_index]
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result


def vigenere_cipher(text, key, encrypt=True):
    alphabet = string.ascii_lowercase
    key = key.lower()  # Ensure key is lowercase
    result = ""
    key_index = 0

    text = text.lower()  # Convert everything to lowercase

    for char in text:
        if char in alphabet:
            shift = alphabet.index(key[key_index % len(key)])
            shift = shift if encrypt else -shift  # Reverse shift for decryption
            new_index = (alphabet.index(char) + shift) % 26
            result += alphabet[new_index]
            key_index += 1  # Move to next key character
        else:
            result += char  # Keep non-alphabetic characters unchanged

    return result


def main():
    while True:
        print("\nChoose an encryption method:")
        print("1 - Caesar Cipher")
        print("2 - Vigenère Cipher")
        print("3 - Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            mode = input("Encrypt or Decrypt? (E/D): ").strip().lower()
            encrypt = mode == "e"
            print("Result:", caesar_cipher(text, shift, encrypt))

        elif choice == "2":
            text = input("Enter text: ")
            key = input("Enter key (a word): ")
            mode = input("Encrypt or Decrypt? (E/D): ").strip().lower()
            encrypt = mode == "e"
            print("Result:", vigenere_cipher(text, key, encrypt))

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
