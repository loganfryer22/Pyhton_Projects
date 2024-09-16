import tkinter as tk
import requests
import random

# List of symbols
symbols = ["!", "$"]

def generate_dino_pass():
    response = requests.get("http://www.dinopass.com/password/simple")
    password = response.text.strip()

    # Capitalize the first letter and add a random symbol at the end
    random_symbol = random.choice(symbols)
    modified_password = password.capitalize() + random_symbol

    # Update the textbox with the generated password
    password_textbox.delete(0, tk.END)  # Clear previous content
    password_textbox.insert(0, modified_password)

# Create the main window
window = tk.Tk()
window.title("DinoPass Generator")

# Create a label
label = tk.Label(window, text="Generated Password:")
label.pack()

# Create a textbox to display the password
password_textbox = tk.Entry(window, width=30)
password_textbox.pack()

# Create a button to trigger password generation
generate_button = tk.Button(window, text="Generate", command=generate_dino_pass)
generate_button.pack()

# Start the GUI event loop
window.mainloop()