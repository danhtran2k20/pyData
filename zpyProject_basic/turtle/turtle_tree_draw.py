# https://stackoverflow.com/questions/25083377/set-no-animation-in-turtle-python-3-4
from turtle import Screen, Turtle
from random import randrange

PEN_SIZE = 8


def tree(branch_length, turtle, pen_size):
    if branch_length < 5:
        return

    angle = randrange(5, 35)
    double_angle = angle * 2
    sub_length = branch_length - randrange(1, 19)

    turtle.pensize(pen_size)
    pen_size *= 0.8

    turtle.forward(branch_length)
    turtle.right(angle)
    tree(sub_length, turtle, pen_size)
    turtle.left(double_angle)
    tree(sub_length, turtle, pen_size)
    turtle.right(angle)
    turtle.backward(branch_length)


def main():
    myWin = Screen()
    yertle = Turtle(visible=False)

    yertle.left(90)
    yertle.penup()
    yertle.backward(170)
    yertle.pendown()

    myWin.tracer(False)
    tree(randrange(40, 47), yertle, PEN_SIZE)
    myWin.tracer(True)

    myWin.exitonclick()


main()
