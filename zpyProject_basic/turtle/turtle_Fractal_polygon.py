# How to Think like a Computer Scientist: Python 3
import turtle
import math


def turtleFractal(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            turtleFractal(turtle, order - 1, size / 3)
            turtle.left(angle)


def turtleSnowflake(turtle, order, size):
    if order == 0:
        for angle in [60, -120, -120]:
            turtle.left(angle)
            turtleFractal(turtle, 0, size)
    else:
        for angle in [60, -120, -120]:
            turtle.left(angle)
            turtleFractal(turtle, order, size / 3)


def turtleFracLine(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in rotateLineAngle:
            turtleFracLine(turtle, order - 1, size * ratio_alpha)
            turtle.left(angle)


alpha, beta, direction = None, None, ""
# input
(order, size, direction, polygon) = (9, 400, "", 4)
alpha = 5
# beta = 60
# angle for polygon
polyAngle = 180 * (polygon - 2) / polygon
polyComAngle = 180 - polyAngle
polyTurtleAngle = []
for i in range(polygon):
    polyTurtleAngle.append(polyComAngle)
polyTurtleAngle[polygon - 1] = 0

# turtle start position
preMove = size / (2 * round(math.cos(math.radians(polyAngle / 2)), 4))
preAngle = 180 - polyAngle / 2
# angle for fractal
if alpha:
    beta = 90 - alpha
if beta:
    alpha = 90 - beta
rotateLineAngle = [beta, -180 + 2 * alpha, beta, 0]
if direction.lower() == "domyWin":
    rotateLineAngle = [-x for x in rotateLineAngle]


# calculate ratio
roundNum = 4
ratio_alpha = round(1 / (2 * (1 + math.sin(math.radians(alpha)))), roundNum)
ratio_beta = round(1 / (2 * (1 + math.cos(math.radians(beta)))), roundNum)


# Setup interface
myWin = turtle.Screen()
alex = turtle.Turtle(visible=False)
# alex.speed(0)
# pre position for center polygon
alex.penup()
alex.right(preAngle)
alex.forward(preMove)
alex.left(preAngle)
alex.pendown()
myWin.tracer(False)

# draw Fractal with turtle
# turtleFractal(alex, 0, 300)
# turtleSnowflake(alex, 2, 600)

# more generalization


# turtleFracLine(alex, order, size)
# more generalization

for angle in polyTurtleAngle:
    turtleFracLine(alex, order, size)
    # alex.forward(size)
    alex.left(angle)
myWin.tracer(True)
myWin.mainloop()
