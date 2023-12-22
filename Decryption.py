import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

human_input = input("What is the key?  ")
human_input = list(human_input)
key = human_input.copy()


cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = human_input.index(letter)
    plain_text += chars[index]

# print(f"Encrypted message: {cipher_text}")
print(f"Original message : {plain_text}")
