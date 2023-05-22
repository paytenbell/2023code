import turtle
import random

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def roll(sides):
    dice=random.randrange(sides)+1
    return(dice)

def drawSpiral(myTurtle,linelen):
    myTurtle.forward(linelen)
    myTurtle.left(33)
    drawSpiral(myTurtle, linelen-10)

drawSpiral (myTurtle,roll(100))
myWin.exitclick()
