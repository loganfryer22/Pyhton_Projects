import random  # Import the random module
import string  # Import the string module

chars = " " + string.punctuation + string.digits + string.ascii_letters  # Define all possible characters
chars = list(chars)  # Convert the string to a list of characters
key = chars.copy()  # Copy the list of characters to create a key

random.shuffle(key)  # Shuffle the key
unlisted_key = ''.join(key)  # Convert the key back to a string
print("The key is: ", unlisted_key)  # Print the key
key = list(key)  # Convert the key back to a list

plain_text = input("Enter a message to encrypt: ")  # Get the message to encrypt from the user
cipher_text = ""  # Initialize the cipher text

for letter in plain_text:  # For each letter in the message
    index = chars.index(letter)  # Find the index of the letter in the list of characters
    cipher_text += key[index]  # Add the corresponding character from the key to the cipher text

print(f"cipher text : {cipher_text}")  # Print the cipher text
