
import re

# Global variables
last_encrypted = ""
last_key = ""

def prepare_text(text):
    text = re.sub(r'[^A-Za-z]', '', text).upper().replace('J', 'I')
    prepared = ''
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i + 1]
        else:
            b = 'X'
        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared

def create_playfair_matrix(key):
    key = re.sub(r'[^A-Za-z]', '', key).upper().replace('J', 'I')
    seen = set()
    matrix = []
    for char in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_encrypt(text, key):
    matrix = create_playfair_matrix(key)
    text = prepare_text(text)
    encrypted = ''
    for i in range(0, len(text), 2):
        encrypted += encrypt_pair(matrix, text[i], text[i+1])
    return encrypted

def playfair_decrypt(text, key):
    # Preprocess input text to be case-insensitive and handle 'J's
    text = re.sub(r'[^A-Za-z]', '', text).upper().replace('J', 'I')  # NEW: Convert to uppercase and replace J with I
    matrix = create_playfair_matrix(key)
    decrypted = ''
    for i in range(0, len(text), 2):
        if i + 1 >= len(text):  # Ensure even length (append 'X' if needed)
            text += 'X'
        decrypted += decrypt_pair(matrix, text[i], text[i+1])
    
    cleaned_text = ''
    i = 0
    while i < len(decrypted):
        if i < len(decrypted) - 1 and decrypted[i+1] == 'X' and (i == len(decrypted)-1 or decrypted[i] != decrypted[i+2]):
            cleaned_text += decrypted[i]
            i += 2
        else:
            cleaned_text += decrypted[i]
            i += 1
    return cleaned_text.lower()

if __name__ == "__main__":
    while True:
        print("\nChoose an option:")
        print("1 - Playfair Cipher Encryption")
        print("2 - Playfair Cipher Decryption")
        print("3 - Exit")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
        elif choice not in ['1', '2']:
            print("Invalid choice! Please enter 1, 2, or 3.")
            continue

        if choice == '1':
            last_key = input("\nEnter the Playfair Cipher key: ").strip()
            message = input("Enter the message to encrypt: ").strip()
            last_encrypted = playfair_encrypt(message, last_key)
            print(f"Encrypted text: {last_encrypted}")

        elif choice == '2':
            if last_encrypted and last_key:
                use_last = input(f"Use last encrypted text '{last_encrypted}' and key '{last_key}'? (yes/no): ").strip().lower()
                if use_last == 'yes':
                    result = playfair_decrypt(last_encrypted, last_key)
                else:
                    last_key = input("Enter the Playfair Cipher key: ").strip()
                    ciphertext = input("Enter the text to decrypt: ").strip()
                    result = playfair_decrypt(ciphertext, last_key)
            else:
                last_key = input("Enter the Playfair Cipher key: ").strip()
                ciphertext = input("Enter the text to decrypt: ").strip()
                result = playfair_decrypt(ciphertext, last_key)
            
            print(f"Decrypted text: {result}")

        restart = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Exiting the program. Goodbye!")
            break
