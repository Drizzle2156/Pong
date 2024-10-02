# Simple Pong in Python3 for beginners
# Part 1: Getting Started

import turtle  # turtle is a built in module from the standard Python library
import os  # provides functions for interacting with the operating system


wn = turtle.Screen()  # wn is window
wn.title("Pong by @BillyNoy")
wn.bgcolor("black")  # background color
wn.setup(width=800, height=600)  # pixels
wn.tracer(0)

# keeping track of score
score_a = 0
score_b = 0


# Paddle A is the LEFT PADDLE,
#  the width is vertical, length is horizontal default pixel size of objects in turtle is 20 vertical, 20 horizontal
paddle_a = turtle.Turtle()  # create the paddle a object
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# 100 = 20 pixels * stretch_wid and 20 = 20 pixels * stretch_len
paddle_a.penup()
paddle_a.goto(-350, 0)  # x, y corrdinates, WE SET IT TO -350
# Paddle B IS THE RIGHT PADDLE
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)  # remove - to move to ri

# Ball
ball = turtle.Turtle()
ball.speed(0)  # animation speed
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Define movement attributes for the ball
ball.dx = 1  # Horizontal speed, goes right
ball.dy = 1  # Vertical speed, goes up

# Pen -> this is a new turtle object, showing the scoring txt
pen = turtle.Turtle()
pen.speed(0)
pen.color("purple")
pen.penup()  # turtle will not leave a trail as it moves
pen.hideturtle()  # dont want to see, only the txt that it writes
pen.goto(0, 260)  # x, y corrdinate
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# 2nd turtle object, just for win or loss messages
endmsg = turtle.Turtle()
endmsg.color("gold")
endmsg.left(90)
endmsg.goto(0, -25)
# Functions to move the paddles with arrow keys

# 3rd turtle object
secondpen = turtle.Turtle()
secondpen.shape("classic")
secondpen.speed(0)
secondpen.color("green")
secondpen.hideturtle
secondpen.penup()
secondpen.goto(0, -260)
secondpen.write("I'm at John Deere ISG!", font=("Trade Gothic", 40))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard bindings with the movement functions
wn.listen()  # listen for keyboard inputs
# when user presses w, call the function paddle_a_up()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop -> mechanics of how the ball moves and bounces from the paddles

while True:
    wn.update()

    # how to move the ball
    ball.setx(ball.xcor() + ball.dx)
    # .xcor is the current x coordinate. dx and dy need to be defined after creating ball object to avoid the attribute error
    ball.sety(ball.ycor() + ball.dy)

    # border checking, done by comparing the ball's y coordinate.
    # compare the balls y coordinate, once it gets to a certain coordinate we want it to bounce from the top. picked 290 because the height is 300, and 290 is just below that, and makes it still visible within the window
    if ball.ycor() > 290:  # if current ball y coordinate is greater than 290
        ball.sety(290)  # gets set back to 290
        ball.dy *= -1  # this reverses the direction
        # plays the sound file, & gets rid of the delay
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:  # if current ball y coordinate is less than -290. Remeber that the further down its more negative
        ball.sety(-290)  # gets set back to -290
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    # left and right border deflection, but we wouldnt use this. remember that width is 800, -400 left, 400 right
    # if ball.xcor() > 390:
    #     ball.setx(390)
    #     ball.dx *= -1

    # if ball.xcor() < -390:
    #     ball.setx(-390)
    #     ball.dx *= -1

    # left and right border resets ball to middle of the coordinate plane, it goes out and counts as a score for player on opposite side.

    # original scoring logic
    # B player score
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1  # this alone doesnt make the pen object increment
        pen.clear()  # so that the updated scores dont write on top of the 0
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))
        # if score_b == 5
        # pen.write("Player B wins! ")

    # A player score
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))


# new testable scoring function

# Inside Pong1.py

    # def update_score(ball_x, score_a, score_b):
    #    # Update the score depending on the position of the ball.

    #     if ball_x > 390:  # Ball goes out on the right side
    #         ball.goto(0, 0)
    #         ball.dx *= -1
    #         score_a += 1
    #         pen.clear()
    #         pen.write("Player A: {} Player B: {}".format(
    #             score_a, score_b), align="center", font=("Courier", 24, "normal"))
    #         return score_a, score_b
    #     elif ball_x < -390:  # Ball goes out on the left side
    #         score_b += 1
    #         return score_a, score_b
    #     return score_a, score_b


# right paddle B collision logic - check notes
# paddle is 100 vertical, 20 horizontal. choose 340 because its slightly away from 350  which is the coordinates of the paddle.
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        os.system("afplay bounce.wav&")
        ball.dx *= -1

# # added this additional condition if ball gets behind the paddle to avoid it constantly bouncing on right side edge without going out
# # and ball.xcor() < 350)
# # ball.setx(340)

# # left paddle A collision logic, flip the conditions for x coordinates
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        os.system("afplay bounce.wav&")
        ball.dx *= -1
