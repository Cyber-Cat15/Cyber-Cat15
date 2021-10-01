from turtlr import *

bgcolor("black")
speed(3)

for i in range(7):
    for color in ('red','cyan','white','magenta','yellow','purple'):
        color(color)
        circle(120)
        right(10)
        
hideturtle()
