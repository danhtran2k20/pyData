# How to Think like a Computer Scientist: Python 3
import turtle
import math


def turtleFracLine(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for index, angle in enumerate(rotateLineAngle):
            if index == 0 or index == len(rotateLineAngle) - 1:
                turtleFracLine(turtle, order - 1, size * ratio_line)
            else:
                turtleFracLine(turtle, order - 1, size * ratio_frac)
            turtle.left(angle)


# input, change only inside this
inputFractal = {
    # polygon size and degree
    "size": 200,
    "polygonSide": 5,
    # Fractal input
    "order": 6,
    "direction": "down",
    "ratioFracLine": 2,  # s2 = s1 * ratioFracLine
    "alpha": 75,
    # animation on or off
    "animation": False,
    "animationSpeed": 0,
}
print("inputFractal:", inputFractal)
# Unpacking dict to var name by key
inputName = [
    "size",
    "polygonSide",
    "order",
    "direction",
    "ratioFracLine",
    "alpha",
    "animation",
    "animationSpeed",
]
(
    size,
    polygonSide,
    order,
    direction,
    ratioFracLine,
    alpha,
    animation,
    animationSpeed,
) = (inputFractal[i] for i in inputName)

# angle for polygon
polyAngle = 180 * (polygonSide - 2) / polygonSide
polyComAngle = 180 - polyAngle
polyTurtleAngle = []
for i in range(polygonSide):
    polyTurtleAngle.append(polyComAngle)
polyTurtleAngle[polygonSide - 1] = 0

# turtle start position base on polygon angle
cos_polyAngle = math.cos(math.radians(polyAngle / 2))
preMove = size / (2 * round(cos_polyAngle, 2))
preAngle = 180 - polyAngle / 2
# angle for fractal
rotateLineAngle = [alpha, -2 * alpha, alpha, 0]
if direction.lower() == "down":
    rotateLineAngle = [-x for x in rotateLineAngle]


# calculate ratio for turtle move
# s1 + prj_s2     = size /2
# s1 + s2*cos_a   = s/2
# s1 + s1*cos_a*k = s/2
# k = (1 + r*cos_a)
# s1  = s /(2k)
# s2 = rs1 = s *(r/(2k))

cos_alpha = math.cos(math.radians(alpha))
temp_ratio = 1 + round(ratioFracLine * cos_alpha, 2)
ratio_line = 1 / (2 * temp_ratio)
ratio_frac = ratioFracLine * ratio_line

# Setup interface
myWin = turtle.Screen()
if not animation:
    alex = turtle.Turtle(visible=False)
else:
    alex = turtle.Turtle()
    alex.speed(animationSpeed)

# pre position for center polygon
alex.stamp()
alex.penup()
alex.right(preAngle)
alex.forward(preMove)
alex.left(preAngle)
alex.pendown()
alex.stamp()
if not animation:
    myWin.tracer(False)
for angle in polyTurtleAngle:
    turtleFracLine(alex, order, size)
    alex.left(angle)
if not animation:
    myWin.tracer(True)
myWin.mainloop()
