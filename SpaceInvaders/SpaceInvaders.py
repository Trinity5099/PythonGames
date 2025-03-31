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











delay = input("press enter to finish.")