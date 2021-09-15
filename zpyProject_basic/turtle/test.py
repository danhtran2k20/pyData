import turtle
import math

length, depth, animation = 550, 5, False
print("length, depth, animation:", length, depth, animation)
# CONST
polygonSide = 3


def draw_sierpinski(turtle, length, depth):
    if depth == 0:
        for _ in range(0, 3):
            turtle.fd(length)
            turtle.left(120)
    else:
        draw_sierpinski(turtle, length / 2, depth - 1)
        turtle.fd(length / 2)
        draw_sierpinski(turtle, length / 2, depth - 1)
        turtle.bk(length / 2)
        turtle.left(60)
        turtle.fd(length / 2)
        turtle.right(60)
        draw_sierpinski(turtle, length / 2, depth - 1)
        turtle.left(60)
        turtle.bk(length / 2)
        turtle.right(60)


def start_position(turtle, length, polygonSide):
    # turtle start position base on polygon angle
    polyAngle = 180 * (polygonSide - 2) / polygonSide
    half_polyAngle = polyAngle / 2
    cos_halfPolyAngle = math.cos(math.radians(half_polyAngle))
    # length = 2*radiusPolygon*cos_halfPolyAngle
    preMove = length / (2 * round(cos_halfPolyAngle, 2))
    turtle.penup()
    turtle.left(half_polyAngle)
    turtle.bk(preMove)
    turtle.left(-half_polyAngle)
    turtle.pendown()


window = turtle.Screen()
if not animation:
    sierpinski_Turtle = turtle.Turtle(visible=False)
    window.tracer(False)
else:
    sierpinski_Turtle = turtle.Turtle()
    sierpinski_Turtle.speed(0)
start_position(sierpinski_Turtle, length, polygonSide)
draw_sierpinski(sierpinski_Turtle, length, depth)
if not animation:
    window.tracer(True)
window.exitonclick()
