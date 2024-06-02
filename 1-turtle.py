#import
import turtle
import time

#reset
turtle.showturtle()
turtle.pendown
color = ['blue', 'red', 'yellow', 'purple']

#draw 4 circle and triangles
for i in range(4):
    turtle.color(color[i])
    turtle.circle(25)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.goto(0,0)

#reset
turtle.penup()
turtle.forward(50)
turtle.pendown()

#draw big square
turtle.color("black")
turtle.left(90)
turtle.forward(50)
for i in range(3):
    turtle.left(90)
    turtle.forward(100)
turtle.left(90)
turtle.forward(50)

#sign
turtle.penup()
turtle.goto(100,-100)
turtle.write("by Yexiaxingkong233")
turtle.goto(100,-110)
turtle.write("2024.6.2")
turtle.goto(100,-120)
turtle.write("Hello world!")

#hide turtle
turtle.hideturtle()

#sleep for ever
while True:
    time.sleep(1)
