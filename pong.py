import turtle  # Import the turtle module

wn = turtle.Screen()  # Create a screen
wn.title("Pong by Logan Fryer")  # Set the title of the screen
wn.bgcolor("black")  # Set the background color of the screen
wn.setup(width=800, height=600)  # Set the size of the screen
wn.tracer(0)  # Turn off screen updates

# Initialize scores for both players
score_a = 0
score_b = 0

# Create Paddle A
paddle_a = turtle.Turtle()  # Create a new turtle object
paddle_a.speed(0)  # Set the speed of the paddle
paddle_a.shape("square")  # Set the shape of the paddle
paddle_a.color("white")  # Set the color of the paddle
paddle_a.shapesize(stretch_wid=6, stretch_len=1)  # Set the size of the paddle
paddle_a.penup()  # Lift the pen up so the paddle doesn't draw anything
paddle_a.goto(-350, 0)  # Move the paddle to its starting position

# Create Paddle B
paddle_b = turtle.Turtle()  # Create a new turtle object
paddle_b.speed(0)  # Set the speed of the paddle
paddle_b.shape("square")  # Set the shape of the paddle
paddle_b.color("white")  # Set the color of the paddle
paddle_b.shapesize(stretch_wid=6, stretch_len=1)  # Set the size of the paddle
paddle_b.penup()  # Lift the pen up so the paddle doesn't draw anything
paddle_b.goto(350, 0)  # Move the paddle to its starting position

# Create the ball
ball = turtle.Turtle()  # Create a new turtle object
ball.speed(0)  # Set the speed of the ball
ball.shape("square")  # Set the shape of the ball
ball.color("white")  # Set the color of the ball
ball.penup()  # Lift the pen up so the ball doesn't draw anything
ball.goto(0, 0)  # Move the ball to the center of the screen
ball.dx = .085  # Set the amount the ball moves in the x direction each time it moves
ball.dy = .085  # Set the amount the ball moves in the y direction each time it moves

# Create the scoreboard
scoreboard = turtle.Turtle()  # Create a new turtle object
scoreboard.speed(0)  # Set the speed of the scoreboard
scoreboard.color("white")  # Set the color of the scoreboard
scoreboard.penup()  # Lift the pen up so the scoreboard doesn't draw anything
scoreboard.hideturtle()  # Hide the turtle so only the text is seen
scoreboard.goto(0, 260)  # Move the scoreboard to the top of the screen
scoreboard.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))  # Write the initial


# score

# Function to update the score display
def update_score():
    scoreboard.clear()  # Clear the current score
    scoreboard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                     font=("Courier", 24, "normal"))  # Write the new score


# Function to check if the ball has hit a boundary
def check_boundary():
    global score_a, score_b  # Declare score_a and score_b as global variables
    if ball.xcor() > 395:  # If the ball hits the right boundary
        score_a += 1  # Increment Player A's score
        update_score()  # Update the score display
    elif ball.xcor() < -395:  # If the ball hits the left boundary
        score_b += 1  # Increment Player B's score
        update_score()  # Update the score display


# Functions to move the paddles
def paddle_a_up():
    if paddle_a.ycor() <= 230:  # If Paddle A is not at the top boundary
        paddle_a.sety(paddle_a.ycor() + 20)  # Move Paddle A up


def paddle_a_down():
    if paddle_a.ycor() >= -230:  # If Paddle A is not at the bottom boundary
        paddle_a.sety(paddle_a.ycor() - 20)  # Move Paddle A down


def paddle_b_up():
    if paddle_b.ycor() <= 230:  # If Paddle B is not at the top boundary
        paddle_b.sety(paddle_b.ycor() + 20)  # Move Paddle B up


def paddle_b_down():
    if paddle_b.ycor() >= -230:  # If Paddle B is not at the bottom boundary
        paddle_b.sety(paddle_b.ycor() - 20)  # Move Paddle B down


# Keyboard bindings
wn.listen()  # Make the window listen for key presses
wn.onkeypress(paddle_a_up, "w")  # Call paddle_a_up when 'w' is pressed
wn.onkeypress(paddle_a_down, "s")  # Call paddle_a_down when 's' is pressed
wn.onkeypress(paddle_b_up, "Up")  # Call paddle_b_up when 'Up' is pressed
wn.onkeypress(paddle_b_down, "Down")  # Call paddle_b_down when 'Down' is pressed

# Main game loop
while True:
    wn.update()  # Update the screen
    check_boundary()  # Check if the ball has hit a boundary

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)  # Move the ball in the x direction
    ball.sety(ball.ycor() - ball.dy)  # Move the ball in the y direction

    # Border checking
    if ball.ycor() > 290:  # If the ball hits the top boundary
        ball.sety(290)  # Set the ball's y coordinate to 290
        ball.dy *= -1  # Reverse the direction of the ball

    if ball.ycor() < -280:  # If the ball hits the bottom boundary
        ball.sety(-280)  # Set the ball's y coordinate to -280
        ball.dy *= -1  # Reverse the direction of the ball

    if ball.xcor() > 395:  # If the ball hits the right boundary
        score_a += 1  # Increment Player A's score
        paddle_a.goto(-350, 0)  # Reset Paddle A's position
        paddle_b.goto(350, 0)  # Reset Paddle B's position
        ball.goto(0, 0)  # Reset the ball's position
        ball.dx *= -1  # Reverse the direction of the ball
        ball.dy *= 1  # Keep the ball's y direction the same
        update_score()  # Update the score display

    if ball.xcor() < -395:  # If the ball hits the left boundary
        score_b += 1  # Increment Player B's score
        paddle_a.goto(-350, 0)  # Reset Paddle A's position
        paddle_b.goto(350, 0)  # Reset Paddle B's position
        ball.goto(0, 0)  # Reset the ball's position
        ball.dx *= -1  # Reverse the direction of the ball
        ball.dy *= -1  # Reverse the direction of the ball
        update_score()  # Update the score display

    # Paddle and ball collisions
    if (330 < ball.xcor() < 360) and (paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60):  # If the ball hits
        # Paddle B
        ball.setx(330)  # Set the ball's x coordinate to 330
        ball.dx *= -1  # Reverse the direction of the ball
    if (-330 > ball.xcor() > -360) and (paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60):  # If the ball
        # hits Paddle A
        ball.setx(-330)  # Set the ball's x coordinate to -330
        ball.dx *= -1  # Reverse the direction of the ball
