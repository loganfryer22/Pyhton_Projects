import secrets
import string
import random

generating = True

while generating:

    password = ""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    # special = string.punctuation
    special = "!@#$%&"
    allChars = lower + upper + digits + special

    passwordlength = int(input("How long of password?: "))
    minupper = int(input('Minimum Upper case letter?: '))
    minlower = int(input('Minimum Lower case letters?: '))
    mindigs = int(input('Minimum Digits?: '))
    minspecial = int(input('Minimum Special characters?: '))

    for i in range(minupper):
        password += "".join(random.choice(secrets.choice(upper)))

    for i in range(minlower):
        password += "".join(random.choice(secrets.choice(lower)))

    for i in range(mindigs):
        password += "".join(random.choice(secrets.choice(digits)))

    for i in range(minspecial):
        password += "".join(random.choice(secrets.choice(special)))

    remaining = passwordlength - minlower - minupper - mindigs - minspecial

    for i in range(remaining):
        password += "".join(random.choice(secrets.choice(allChars)))

    password = list(password)
    random.shuffle(password)
    print("".join(password))

    if not input("Need another password? (y/n): ").lower() == 'y':
        generating = False

print("Don't forget it!")
