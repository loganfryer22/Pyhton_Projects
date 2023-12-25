def area_of_circle():  # Function to calculate the area of a circle
    r = float(input("What is the radius? "))  # Get the radius from the user
    pi = 3.14  # Define the value of pi
    area = pi * (r ** 2)  # Calculate the area
    print(area)  # Print the area


def life_calculator():  # Function to calculate the user's age in different units
    age = int(input("How old are you? "))  # Get the user's age
    years = age  # Age in years
    months = age * 12  # Age in months
    days = age * 365  # Age in days
    weeks = age * 52  # Age in weeks
    print(f"Years: {years}", f"Months: {months}", f"Days: {days}", f"Weeks: {weeks}")  # Print the age in different
    # units


def index_search():  # Function to search for a word in a file
    repeat = True  # Control variable for the loop
    while repeat:  # Start a loop that continues as long as 'repeat' is True
        search = input("What name are you looking for?: ").lower()  # Get the search word from the user

        with open("C:\\Users\\logan\\OneDrive\\Documents\\WORK STUFF\\list_of_names.txt", 'r') as file:  # Open the file
            file = file.read().lower()  # Read the file and convert it to lowercase

        output = search in file  # Check if the search word is in the file
        if output:  # If the search word is in the file
            index = file.index(search)  # Find the index of the search word in the file
            print(f"{index}")  # Print the index
            print(output)  # Print True
        else:  # If the search word is not in the file
            print("Not found")  # Print "Not found"
            print(output)  # Print False

        if input("Another one? any key = yes, no = quit ").lower() == 'no' or 'n':  # Ask the user if they want to
            # search again
            repeat = False  # If they enter 'no', end the loop


def search_dictionary():  # Function to search for a word in a dictionary
    import requests  # Import the requests module
    repeat = True  # Control variable for the loop
    while repeat:  # Start a loop that continues as long as 'repeat' is True

        url = "https://raw.githubusercontent.com/sujithps/Dictionary/master/Oxford%20English%20Dictionary.txt"  # URL
        # of the dictionary
        response = requests.get(url)  # Send a GET request to the URL
        file = response.text.lower()  # Get the text content of the response and convert it to lowercase

        search = input("What are you looking for?  ")  # Get the search word from the user
        count = file.count(search)  # Count the occurrences of the search word in the dictionary
        print(f"There are {count} {search} in the dictionary")  # Print the number of occurrences

        if input("Another one? n = no  ").lower() == "n" or "no":  # Ask the user if they want to search again
            repeat = False  # If they enter 'n', end the loop


def format_name_age():  # Function to format the user's name and age
    first_name = input("What is your first name?   ")  # Get the user's first name
    last_name = input("What is your last name?  ")  # Get the user's last name
    age = input("What is your age?   ")  # Get the user's age

    print("Name is {} {} and I am {} years old".format(first_name, last_name, age))  # Print the formatted string


