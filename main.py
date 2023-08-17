# if you import like that you should write each time like turtle.Turtle()
#import turtle
#tim = turtle.Turtle()

#You can write easily if you do:

from turtle import Turtle
tim = Turtle()

from turtle import Screen

tim.shape("turtle")
tim.color("red")
screen=Screen() #This is a class, so we need to create an object of it and then use its methods/attributes (methods
for _ in range(5):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)




























screen = Screen()
screen.exitonclick()