def rock_paper_scissors():
    import random  # Import the random module

    options = ("rock", "paper", "scissors")  # Define the options for the game
    playing = True  # Initialize a variable to control the game loop
    counter = 0  # Initialize a counter for invalid inputs
    player_counter = 0  # Initialize a counter for player's attempts

    while playing:  # Start the game loop

        output = 0  # Initialize a variable to store the game result
        player = None  # Initialize a variable to store the player's choice
        computer = random.choice(options)  # The computer makes a random choice

        while player not in options:  # Keep asking for the player's choice until it's valid
            player = input("Enter a choice (rock, paper, scissors): ").lower()  # Get the player's choice
            if player not in options:  # If the player's choice is not valid
                print("Invalid")  # Print an error message
                counter += 1  # Increment the counter
                if counter == 5:  # If the counter reaches 5
                    playing = False  # End the game loop
                    break  # Break the inner loop

        if not playing:  # If the game has ended, break the outer loop
            break

        player_counter += 1  # Increment the player's attempts counter
        print(f"player: {player}")  # Print the player's choice
        print(f"computer: {computer}")  # Print the computer's choice

        if player == computer:  # If the player and the computer made the same choice, it's a tie
            print("It's a TIE!")

        elif player == 'rock' and computer == 'scissors':  # If the player chose rock and the computer chose scissors,
                                                           # the player wins
            output += 1
            print("You WIN!")

        elif player == "paper" and computer == "rock":  # If the player chose paper and the computer chose rock,
                                                        # the player wins
            output += 1
            print("You WIN!")

        elif player == 'scissors' and computer == "paper":  # If the player chose scissors and the computer chose paper,
                                                            # the player wins
            output += 1
            print("You WIN!")

        else:  # In all other cases, the player loses
            print('You LOSE!')

        if output == 1:  # If the player won, end the game
            playing = False

    if counter == 5:  # If the game ended due to too many invalid inputs
        print("Too many invalid inputs")
    else:  # If the game ended normally
        print("Thanks for playing!")
        print(f"it took {player_counter} attempt(s)")  # Print the number of attempts it took the player to win
        
rock_paper_scissors()  # runs the program

