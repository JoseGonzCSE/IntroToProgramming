# This program produces a snowman
# Inputs: none 
# Outputs: a snowman
# # Written by: Jose Gonzalez 
# Modified Date: Feb,27,2020

import turtle
t=turtle.Turtle()

def Body(radius,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(radius)

Body(50,0,0)
Body(30,0,100)
Body(15,0,160)

def Arm(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.left(300)

Arm(-30,130)