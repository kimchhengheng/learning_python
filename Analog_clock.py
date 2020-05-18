import turtle
import time

wn = turtle.Screen()  # Screen is the class
wn.title("Analog by kimchheng heng")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)  # turn off the animation stop the win from update manual
# turn off animate by tracer(0) and update


pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(h, m, s):
    # draw clock face
    global pen
    pen.up()
    pen.goto(0, -210)
    pen.setheading(0)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    # draw the lines for the hours
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    # draw the 12 hour of the clock
    for i in range(12):
        pen.fd(210)
        pen.pendown()
        pen.color("blue")
        pen.bk(30)  # forward
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)  # rotate

    # draw the min in the clock
    for i in range(60):
        if i % 5 != 0:
            pen.fd(210)
            pen.pendown()
            pen.color("Navy Blue")
            pen.bk(15)  # forward
            pen.penup()
            pen.goto(0, 0)
            pen.rt(6)  # rotate
        else:
            pen.rt(6)

    # draw the hour min sec
    pen.penup()
    pen.goto(0, 0)
    pen.color("orange")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)

    pen.penup()
    pen.goto(0, 0)
    pen.color("pink")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    pen.penup()
    pen.goto(0, 0)
    pen.color("yellow")
    pen.setheading(90)
    angle = (s / 60) * 360  # the angle is 60 for both min and sec just the value of it gonna different
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)


while True:
    # for loop to update the hour min sec
    h = int(time.strftime("%I"))  # %I give the hour
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h, m, s)
    wn.update()  # draw every to memory then pull back to the screen
    time.sleep(1) # sleep for 1 s delay
    pen.clear()

wn.mainloop()  # if i dont, the open and close automatically
