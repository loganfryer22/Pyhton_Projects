import secrets  # For generating cryptographically strong random numbers
import string  # For string constants
import random  # For generating pseudo-random numbers

generating = True  # Control variable for the main loop

while generating:  # Main loop

    password = ""  # Initialize the password string
    lower = string.ascii_lowercase  # All lowercase letters
    upper = string.ascii_uppercase  # All uppercase letters
    digits = string.digits  # All digits
    special = "!@#$%&"  # Special characters
    allChars = lower + upper + digits + special  # All possible characters

    passwordlength = int(input("How long of password?: "))  # Get password length from user
    minupper = int(input('Minimum Upper case letter?: '))  # Get minimum number of uppercase letters from user
    minlower = int(input('Minimum Lower case letters?: '))  # Get minimum number of lowercase letters from user
    mindigs = int(input('Minimum Digits?: '))  # Get minimum number of digits from user
    minspecial = int(input('Minimum Special characters?: '))  # Get minimum number of special characters from user

    for i in range(minupper):  # Add the required number of uppercase letters to the password
        password += "".join(random.choice(secrets.choice(upper)))

    for i in range(minlower):  # Add the required number of lowercase letters to the password
        password += "".join(random.choice(secrets.choice(lower)))

    for i in range(mindigs):  # Add the required number of digits to the password
        password += "".join(random.choice(secrets.choice(digits)))

    for i in range(minspecial):  # Add the required number of special characters to the password
        password += "".join(random.choice(secrets.choice(special)))

    remaining = passwordlength - minlower - minupper - mindigs - minspecial  # Calculate the remaining length of the
                                                                             # password

    for i in range(remaining):  # Add random characters to the password until it reaches the desired length
        password += "".join(random.choice(secrets.choice(allChars)))

    password = list(password)  # Convert the password string to a list
    random.shuffle(password)  # Shuffle the characters in the password
    print("".join(password))  # Print the password

    if not input("Need another password? (y/n): ").lower() == 'y':  # Ask the user if they need another password
        generating = False  # If not, end the main loop

print("Don't forget it!")  # Remind the user to remember their password
