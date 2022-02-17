"""Using turtle to draw a UNC Logo with coloful decorations."""

__author__ = "730473612"

from turtle import Turtle, colormode, done 
colormode(255)


def back_fill(RJ: Turtle, x: float, y: float, red: int, green: int, blue: int) -> None:
    """Fill back of screen with RGB color given."""
    RJ.pencolor("black")
    RJ.fillcolor(red, green, blue)
    RJ.penup()
    RJ.goto(x, y)
    RJ.pendown()
    RJ.begin_fill()
    i: int = 0
    while i < 4:
        RJ.left(90)
        RJ.forward(2000)
        i += 1
    RJ.end_fill()
 

def draw_U(RJ: Turtle, x: float, y: float, red: int, green: int, blue: int) -> None:
    """Draw a U filled with RGB color given."""
    RJ.pencolor(117, 222, 255)
    RJ.fillcolor(red, green, blue)
    RJ.penup()
    RJ.goto(x, y)
    RJ.pendown()
    RJ.begin_fill()
    RJ.right(90)
    RJ.forward(150)
    RJ.left(90)
    RJ.forward(125)
    RJ.left(90)
    RJ.forward(150)
    RJ.left(90)
    RJ.forward(25)
    RJ.left(90)
    RJ.forward(125)
    RJ.right(90)
    RJ.forward(75)
    RJ.right(90)
    RJ.forward(125)
    RJ.left(90)
    RJ.forward(25)
    RJ.end_fill()


def draw_N(RJ: Turtle, x: float, y: float, red: int, green: int, blue: int) -> None:
    """Draw an N filled with RGB color given."""
    RJ.pencolor(117, 222, 255)
    RJ.fillcolor(red, green, blue)
    RJ.penup()
    RJ.goto(x, y)
    RJ.pendown()
    RJ.begin_fill()
    RJ.left(90)
    RJ.forward(150)
    RJ.left(90)
    RJ.forward(25)
    RJ.left(90)    
    RJ.forward(100)
    RJ.right(135)
    RJ.forward(141.4)
    RJ.left(45)
    RJ.forward(25)
    RJ.left(90)
    RJ.forward(150)
    RJ.left(90)
    RJ.forward(25)
    RJ.left(90)
    RJ.forward(100)
    RJ.right(135)
    RJ.forward(141.4)
    RJ.left(45)
    RJ.forward(25)
    RJ.end_fill()


def draw_C(RJ: Turtle, x: float, y: float, red: int, green: int, blue: int) -> None:
    """Draw an C filled with RGB color given."""
    RJ.pencolor(117, 222, 255)
    RJ.fillcolor(red, green, blue)
    RJ.penup()
    RJ.goto(x, y)
    RJ.pendown()
    RJ.begin_fill()
    RJ.left(90)
    RJ.forward(150)
    RJ.left(90)
    RJ.forward(125)
    RJ.left(90)
    RJ.forward(25)
    RJ.left(90)
    RJ.forward(100)
    RJ.right(90)
    RJ.forward(100)
    RJ.right(90)
    RJ.forward(100)
    RJ.left(90)
    RJ.forward(25)
    RJ.left(90)
    RJ.forward(125)
    RJ.end_fill()


def draw_white_dot(RJ: Turtle) -> None:
    """Draw a white polka dot."""
    RJ.dot(20, "white")


def draw_dots_around(RJ: Turtle, x: float, y: float) -> None:
    """Draws white polka dots in pattern around UNC logo."""
    RJ.penup()
    RJ.goto(x, y)
    RJ.pendown()
    while x < 250.0:
        RJ.penup()
        RJ.goto(x, y)
        RJ.pendown()
        draw_white_dot(RJ)
        x += 50
    while y < 125.0:
        RJ.penup()
        RJ.goto(x, y)
        RJ.pendown()
        draw_white_dot(RJ)
        y += 50
    while x > -300.0:
        RJ.penup()
        RJ.goto(x, y)
        RJ.pendown()
        draw_white_dot(RJ)
        x -= 50
    while y > -125.0:
        RJ.penup()
        RJ.goto(x, y)
        RJ.pendown()
        draw_white_dot(RJ)
        y -= 50


def strip(RJ: Turtle, x: float, y: float) -> None:
    """Creates white strip across screen with black outline."""
    RJ.penup()
    RJ.goto(x, y)
    RJ.pendown()
    RJ.color("black", "white")
    RJ.begin_fill()
    RJ.left(180)
    RJ.forward(2000.0)
    RJ.left(90)
    RJ.forward(25)
    RJ.left(90)
    RJ.forward(2000.0)
    RJ.left(90)
    RJ.forward(25)
    RJ.end_fill()
    

def main() -> None:
    """The entrypoint of my scene."""
    rameses: Turtle = Turtle()
    rameses.speed(0)
    back_fill(rameses, 400.0, -400.0, 21, 23, 93)
    draw_U(rameses, -250.0, 75.0, 117, 222, 255)
    draw_N(rameses, -100.0, 75.0, 117, 222, 255)
    draw_C(rameses, 75.0, 75.0, 117, 222, 255)
    draw_dots_around(rameses, -300.0, -125.0)
    strip(rameses, -500.0, 150.0)
    rameses.right(90)
    strip(rameses, -500.0, -175.0)
    done()


if __name__ == "__main__":
    main()