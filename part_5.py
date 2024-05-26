import string
from collections import Counter


# English letter frequency
english_freq = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95,
    'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88,
    'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03,
    'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
}


def decrypt_caesar_cipher(ciphertext, shift):
    decrypted = []
    for char in ciphertext:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted.append(chr(shifted))
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted.append(chr(shifted))
        else:
            decrypted.append(char)
    return ''.join(decrypted)


def calculate_letter_frequency(text):
    text = text.upper()
    letter_counts = Counter(char for char in text if char in string.ascii_uppercase)
    total_letters = sum(letter_counts.values())
    frequency = {char: (count / total_letters) * 100 for char, count in letter_counts.items()}
    return frequency


def chi_squared_stat(observed, expected):
    chi_squared = 0.0
    for char in expected:
        observed_value = observed.get(char, 0)
        expected_value = expected[char]
        chi_squared += ((observed_value - expected_value) ** 2) / expected_value
    return chi_squared


def find_best_shift(ciphertext):
    min_chi_squared = float('inf')
    best_shift = None
    for shift in range(26):
        decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
        observed_freq = calculate_letter_frequency(decrypted_text)
        chi_squared = chi_squared_stat(observed_freq, english_freq)
        if chi_squared < min_chi_squared:
            min_chi_squared = chi_squared
            best_shift = shift
    return best_shift


# Example ciphertext
ciphertext = "Wkh vwdwxh lv exuulhg xqghu d wuhh pdunhg zlwk a rq Foxvwhu Lvodqg- 3"


# Find the best shift
best_shift = find_best_shift(ciphertext)
print(f"Best shift: {best_shift}")


# Decrypt the ciphertext using the best shift
decrypted_text = decrypt_caesar_cipher(ciphertext, best_shift)
print(f"Decrypted text: {decrypted_text}")