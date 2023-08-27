from turtle import Turtle, Screen
import random

timmy = Turtle()
def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    color = timmy.color(R, G, B)


for i in range(3, 9, +1):
    for _ in range(i):
        timmy.forward(100)
        timmy.right(360/i)
        change_color()


screen = Screen()
screen.exitonclick()
