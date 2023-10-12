# This program produces Snowman
# Inputs: none 
# Outputs: Snowman
# Written by: Jose Gonzalez
# Modified Date: Feb,27,2020


import turtle

def main():
  Radian = 50
  Radian2 = 30
  Radian3 = 15  
  base(Radian)
  middle(Radian, Radian2)
  head(Radian3)
  arms()
  Hbase()
  Hat()
 
 #Body
def base(Radian):
  circle(0,0,Radian)

  #Middle
def middle(Radian, Radian2):
  circle(0,Radian + Radian2, Radian2)

   #Head
def head(Radian3):
  circle(0, 125, Radian3)

  
def arms():
  #left 
  line(-30, 80,-80,80)
  #right
  line(30, 80, 80,90)

#Hat Base 
def Hbase():
    square(-30,140)
    square(30,140)
    square(30,135)
    square(-30,135)
    square(-30,140)

# Hat
def Hat():
    square(-15,140)
    square(-15,150)
    square(15,150)
    square(15,140)
    
#circle 
def circle(x,y, radius):
  turtle.penup()
  turtle.goto(x,y - radius)
  turtle.pendown()
  turtle.circle(radius)

#line 
def line(start, starty, end,endy):
  turtle.penup()
  turtle.goto(start, starty)
  turtle.pendown()
  turtle.goto(end, endy)
  turtle.penup()
  
#square
def square(x,y,):
  turtle.goto(x,y)
  turtle.pendown()
main()
