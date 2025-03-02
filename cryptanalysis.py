
from collections import Counter
import string

def letter_frequencies(text):
    # Convert text to lowercase to ensure case insensitivity
    text = text.lower()
    # Filter out non-alphabetic characters
    filtered_text = ''.join(filter(str.isalpha, text))
    # Count the frequency of each character
    counter = Counter(filtered_text)
    # Create a dictionary with all letters initialized to 0
    frequencies = {letter: 0 for letter in string.ascii_lowercase}
    # Update the dictionary with actual frequencies
    frequencies.update(counter)
    return frequencies

# User input
text = input("Enter your text: ")
frequencies = letter_frequencies(text)

# Display results
print("\nLetter Frequencies:")
for letter, freq in frequencies.items():
    print(f"'{letter}': {freq}")

# Find and display the most frequent letter
most_frequent = max(frequencies, key=frequencies.get)
print(f"\nThe most frequent letter is '{most_frequent}' with {frequencies[most_frequent]} occurrences.")
