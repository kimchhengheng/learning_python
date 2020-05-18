import turtle
import time
import random
import winsound

delay = 0.2
segment = []
score = 0
cscore = 0
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.title("kimchheng heng")
wn.bgcolor("green")
wn.tracer(0) # turn off the screen update

pen = turtle.Turtle()
pen.speed(0) # speed 0 is the faster
pen.color("white")
pen.penup()  # dont want to draw line when it is move
pen.hideturtle()  # dont want to see the head arrow
pen.goto(0, 260)
pen.write("Score : 0 High score: 0", align="center", font=("Ariel", 16, "normal"))

# snake and listen to the key board
head = turtle.Turtle()
head.shape("square")
head.speed(0) # animation speed 0 is fastest
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20) # the screen will move too fast not see without delay
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def go_up():
    #global head
    if head.direction != "down":
        head.direction = "up"
def go_down():
    #global head
    if head.direction != "up":
        head.direction = "down"
def go_left():
    #global head
    if head.direction != "right":
        head.direction = "left"
def go_right():
    #global head
    if head.direction != "left":
        head.direction = "right"


# key board binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# the food to eat
food = turtle.Turtle()
food.shape("circle")
food.speed(0) # animation speed 0 is fastest
food.color("red")
food.penup()
food.goto(0, 100)

# collision of head and food using pythagorean to meassure the distance of head and food



# die when hit the border and it self

# update the score and value


# main game loop
while True:
    wn.update()

    # check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        score = len(segment)
        #hide the segments move the availabe segment out of the place
        for seg in segment:
            seg.goto(1000, 1000)
        #clear the segment array
        segment.clear()
        pen.clear()
        pen.write("Score : 0 High score: {}".format(score), align="center", font=("Ariel", 16, "normal"))


    if head.distance(food) < 20:
        # move the food to the random spot of the screen
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # increase the side of the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segment.append(new_segment)

        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # can add the sound of snake collision


    # move the end segments first in reverse order
    # the coord is not always 0 0 since the head it is moving
    for index in range(len(segment)-1, 0, -1): # from len 9 to 0 but exclusive 0
        x = segment[index-1].xcor()
        y = segment[index-1].ycor()
        segment[index].goto(x, y)

    #move segment 0 to where the head is only more than 1
    # first segment gonna move to head
    # first collision of head and food
    if len(segment) > 0:
        x = head.xcor()
        y = head.ycor()
        segment[0].goto(x, y)
    # they are moving fast so we dont know about the loop
    move()

    # check if they hit their self
    # after they move already so <20 mean it hit them self
    for seg in segment:
        if seg.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            # hide the segments move the available segment out of the place
            score = len(segment)
            pen.clear()
            pen.write("Score : 0 High score: {}".format(score), align="center", font=("Ariel", 16, "normal"))
            for seg in segment:
                seg.goto(1000, 1000)
            # clear the segment array
            segment.clear()
    cscore = len(segment)
    pen.clear()
    pen.write("Score : {} High score: {}".format(cscore, score), align="center", font=("Ariel", 16, "normal"))
    time.sleep(delay)

wn.mainloop()