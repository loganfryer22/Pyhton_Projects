

def area_of_circle():
    r = float(input("What is the radius? "))
    pi = 3.14
    area = pi * (r ** 2)
    print(area)


def life_calculator():
    age = int(input("How old are you? "))
    years = age
    months = age * 12
    days = age * 365
    weeks = age * 52
    print(f"Years: {years}", f"Months: {months}", f"Days: {days}", f"Weeks: {weeks}")


def index_search():
    repeat = True
    while repeat:
        search = input("What are you looking for?: ").lower()

        with open("C:\\Users\\logan\\OneDrive\\Documents\\WORK STUFF\\list_of_names.txt", 'r') as file:
            file = file.read().lower()

        output = search in file
        if output:
            index = file.index(search)
            print(f"{index}")
            print(output)
        else:
            print("Not found")
            print(output)

        if input("Another one? any key = yes, no = quit ").lower() == 'no':
            repeat = False


def search_dictionary():  # Define the function search_dictionary
    import requests
    repeat = True  # Initialize a variable 'repeat' to True. This will control the while loop for repeating the search.
    while repeat:  # Start a while loop that continues as long as 'repeat' is True

        url = "https://raw.githubusercontent.com/sujithps/Dictionary/master/Oxford%20English%20Dictionary.txt"
        # Define the URL where the dictionary file is located
        response = requests.get(url)  # Send a GET request to the URL
        file = response.text.lower()  # Get the text content of the response and convert it to lowercase

        search = input("What are you looking for?  ")  # Ask the user for the word they are looking for
        count = file.count(search)  # Count the occurrences of the search word in the dictionary file
        print(f"There are {count} {search} in the dictionary")  # Print the number of occurrences of the search word

        if input("Another one? n = no  ").lower() == "n" or "no":  # Ask the user if they want to search for another
            # word.
            repeat = False  # If they enter 'n' or 'N', set 'repeat' to False


def format_name_age():
    first_name = input("What is your first name?   ")
    last_name = input("What is your last name?  ")
    age = input("What is your age?   ")

    print("Name is {} {} and I am {} years old".format(first_name, last_name, age))


def to_celsius(x):
    return (x - 32) * 5 / 9
