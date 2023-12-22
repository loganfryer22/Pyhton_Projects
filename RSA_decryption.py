import string  # Import the string module

chars = " " + string.punctuation + string.digits + string.ascii_letters  # Define all possible characters
chars = list(chars)  # Convert the string to a list of characters

human_input = input("What is the key?  ")  # Get the key from the user
human_input = list(human_input)  # Convert the key to a list of characters
key = human_input.copy()  # Copy the key

cipher_text = input("Enter a message to decrypt: ")  # Get the cipher text from the user
plain_text = ""  # Initialize the plain text

for letter in cipher_text:  # For each letter in the cipher text
    index = human_input.index(letter)  # Find the index of the letter in the key
    plain_text += chars[index]  # Add the corresponding character from the list of characters to the plain text

print(f"Original message : {plain_text}")  # Print the plain text
