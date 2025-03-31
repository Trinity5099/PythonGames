import turtle
import os
import random
import math

#Setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#borders
border_pen = turtle.Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)


 #creating the player
player= turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.lt(90)
player.setposition(0, -250)

playerspeed = 15

#Moving the player
def move_left():
    x = player.xcor()
    x-= playerspeed
    if x < -280:
        x= -280
    player.setx(x)
def move_right():
    x  = player.xcor()
    x += playerspeed
    if x > 280:
        x= 280
    player.setx(x)


#keybindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")


delay = input("Press enter to finish.")