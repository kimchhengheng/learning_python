import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by kimchheng")
wn.bgcolor("black")  # background color
wn.setup(width=800, height=600)  # size of the window screen
wn.tracer(0)  # speed up the game stop the window from update manually update
# turn off the animation so the ball gonna move by dx fast

# paddle A
paddle_a = turtle.Turtle()  # turtle is module Turtle is the class paddle_a is the object of turtle
paddle_a.speed(0)  # set the speed to maximum
paddle_a.shape("square")
# by default shape is 20 by 20 stretch wid pull the width top to bottom
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("yellow")
paddle_a.penup()  # turtle by definition is draw a line we dont need the line so we pendup
paddle_a.goto(-350, 0)  # want to start specific location 0,0 is the middle

# paddle B
paddle_b = turtle.Turtle()  # turtle is module Turtle is the class paddle_a is the object of turtle
paddle_b.speed(0)  # set the speed to maximum
paddle_b.shape("square")
# by default shape is 20 by 20 stretch wid pull the width top to bottom
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("pink")
paddle_b.penup()  # turtle by definition is draw a line we dont need the line so we pendup
paddle_b.goto(350, 0)  # want to start specific location 0,0 is the middle

# ball

ball = turtle.Turtle()  # turtle is module Turtle is the class paddle_a is the object of turtle
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()  # turtle by definition is draw a line we dont need the line so we pendup
ball.goto(0, 0)  # want to start specific location 0,0 is the middle
ball.dx = 0.15  # change in x coord
ball.dy = 0.15  # change in y coord


# move the paddle according to keyboard should make sure the paddle cannot go off the screen


def paddle_a_up():
    y = paddle_a.ycor()  # return the y corrdinate
    y += 20
    if y < 250:
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # return the y corrdinate
    y -= 20
    if y > -250:
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # return the y corrdinate
    y += 20
    if y < 250:
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # return the y corrdinate
    y -= 20
    if y > -250:
        paddle_b.sety(y)


# score
score_a = 0
score_b = 0
# pen is the turtle to provide the score of player

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()  # dont want to draw line when it is move
pen.hideturtle()  # dont want to see the text
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Ariel", 16, "normal"))
# keyboard binding

wn.listen()  # listen for kb input
wn.onkeypress(paddle_a_up, "w")
# when user press w call function paddle_a up call the function for this listener does not need ()
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




# main game loop

while True:
    wn.update()

    # move the ball every loop it change
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking the top would be 300 bottom is -300 the coordinate is the middle of ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # border checking on the x cor give mark to other
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 16, "normal"))
    # string format {} then .format give the parameter

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 16, "normal"))

    # hit the paddle > 340 it is increment first that why after increase it greater than 340 position of paddle edge tough
    # -10 since coordinate is in the middle of object
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1

    # show the mark of player
