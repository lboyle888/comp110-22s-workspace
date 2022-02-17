"""Practice with python tutrle."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
colormode(255)
leo.color(99, 204, 250)
leo.pencolor(123,76,45)

leo.penup()
leo.goto(-100,-100)
leo.pendown()
leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
done()
