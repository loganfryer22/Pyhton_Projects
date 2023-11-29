import turtle


wn = turtle.Screen()
wn.title("Pong by Logan Fryer")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Create the window
# wn = turtle.Screen()
# wn.title("Pong by Logan Fryer")
# wn.bgcolor("black")
# wn.setup(width=800, height=600)

# Create the start button
# start_button = turtle.Turtle()
# start_button.speed(0)
# start_button.shape("square")
# start_button.color("green")
# start_button.shapesize(stretch_wid=2, stretch_len=6)
# start_button.penup()
# start_button.goto(0, 0)

# score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .085
ball.dy = .085

# Create the scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Update the score
def update_score():
    scoreboard.clear()
    scoreboard.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                     font=("Courier", 24, "normal"))


# Check if the ball has hit a boundary
def check_boundary():
    global score_a, score_b
    if ball.xcor() > 395:
        score_a += 1
        update_score()
    elif ball.xcor() < -395:
        score_b += 1
        update_score()


# Function

def paddle_a_up():
    if paddle_a.ycor() <= 230:
        paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    if paddle_a.ycor() >= -230:
        paddle_a.sety(paddle_a.ycor() - 20)


def paddle_b_up():
    if paddle_b.ycor() <= 230:
        paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    if paddle_b.ycor() >= -230:
        paddle_b.sety(paddle_b.ycor() - 20)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()
    check_boundary()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() - ball.dy)

    # border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 395:
        score_a += 1
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= 1
        update_score()

    if ball.xcor() < -395:
        score_b += 1
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        update_score()

    # paddle and ball collisions
    if (330 < ball.xcor() < 360) and (paddle_b.ycor() + 60 > ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(330)
        ball.dx *= -1
    if (-330 > ball.xcor() > -360) and (paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-330)
        ball.dx *= -1
