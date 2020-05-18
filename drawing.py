import turtle
import random
from turtle import _Screen
import time
import winsound

wn = turtle.Screen()
wn.title("kimchheng heng")
wn.setup(width=700, height=700)
wn.bgcolor("black")
wn.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()  # hide the arrow head of turtule
pen.speed(0)
pen.pensize(3)


def draw(choice):

    if choice == 1:
        draw_1()
        winsound.PlaySound("bounce.wav",  winsound.SND_ASYNC)
    elif choice == 2:
        draw_2()
    elif choice == 3:
        draw_3()
    elif choice == 4:
        draw_4()
    else:
        draw_1()
        draw_2()
        draw_3()
        draw_4()

def draw_1():
    global pen
    pen.penup()
    pen.setheading(90)  # if no set the head even goto the draw continue
    pen.goto(-75, 150)
    pen.color("pink")
    pen.pendown()
    pen.circle(75)
    pen.penup()
    pen.goto(0, 0)


def draw_2():
    global pen
    pen.penup()
    pen.goto(50, 250)
    pen.color("yellow")
    pen.pendown()
    pen.setheading(0)
    pen.fd(150)
    pen.right(90)
    pen.fd(150)
    pen.right(90)
    pen.fd(150)
    pen.right(90)
    pen.fd(150)
    pen.right(90)
    pen.fd(150)
    pen.penup()
    pen.goto(0, 0)


def draw_3():
    global pen
    pen.penup()
    pen.goto(-100, -250)
    pen.color("orange")
    pen.pendown()
    pen.setheading(180)
    pen.rt(60)
    pen.forward(150)
    pen.lt(120)
    pen.fd(150)
    pen.lt(120)
    pen.fd(150)
    pen.penup()
    pen.goto(0, 0)


def draw_4():
    global pen
    pen.penup()
    pen.goto(75, -150)
    pen.color("blue")
    pen.pendown()
    pen.setheading(0)
    pen.forward(150)
    pen.rt(120)
    pen.fd(150)
    pen.rt(120)
    pen.fd(150)  # one triangle
    pen.rt(60)
    pen.fd(150)
    pen.rt(120)
    pen.fd(150)
    pen.penup()
    pen.goto(0, 0)


while True:
    num = random.randint(1, 5)
    draw(num)

    wn.update()  # draw every to memory then pull back to the screen
    time.sleep(1)
    pen.clear()

wn.mainloop()
