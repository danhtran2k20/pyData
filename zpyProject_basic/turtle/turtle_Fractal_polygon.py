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
    "radiusPolygon": 250,
    "polygonSide": 3,
    # Fractal input
    "order": 1,
    "direction": "down",
    "ratio_line": 2/3,
    "alpha": 60,
    # animation on or off
    "circleDraw": True,
    "animation": False,
    "animationSpeed": 1,
}
print("inputFractal:", inputFractal)
# Unpacking dict to var name by key
inputName = [
    "radiusPolygon",
    "polygonSide",
    "order",
    "direction",
    "ratio_line",
    "alpha",
    "animation",
    "animationSpeed",
    "circleDraw",
]
(
    radiusPolygon,
    polygonSide,
    order,
    direction,
    ratio_line,
    alpha,
    animation,
    animationSpeed,
    circleDraw,
) = (inputFractal[i] for i in inputName)

# angle for polygon
polyAngle = 180 * (polygonSide - 2) / polygonSide
polyComAngle = 180 - polyAngle
polyTurtleAngle = []
for i in range(polygonSide):
    polyTurtleAngle.append(polyComAngle)
polyTurtleAngle[polygonSide - 1] = 0

# turtle start position base on polygon angle
half_polyAngle = polyAngle / 2
cos_halfPolyAngle = math.cos(math.radians(half_polyAngle))
size = 2 * radiusPolygon * cos_halfPolyAngle
preMove = size / (2 * round(cos_halfPolyAngle, 2))
# angle for fractal
rotateLineAngle = [alpha, -2 * alpha, alpha, 0]
if direction.lower() == "down":
    rotateLineAngle = [-x for x in rotateLineAngle]


# calculate ratio for turtle move
# s1 + prj_s2     = size /2
# s1 + s2*cos_a   = s/2
# s1 + s1*cos_a*r = s/2
# k = (1 + r*cos_a)
# s1  = s /(2k)
# s2 = rs1 = s *(r/(2k))
# ratio_line = 1 / (2 * temp_ratio)

cos_alpha = math.cos(math.radians(alpha))
ratio_line /= 2
temp_ratio = 1 / 2 - ratio_line
ratio_frac = temp_ratio / (round(cos_alpha, 4))
print("ratio_frac:", ratio_frac)

# Setup interface
myWin = turtle.Screen()
if not animation:
    alex = turtle.Turtle(visible=False)
    myWin.tracer(False)
else:
    alex = turtle.Turtle()
    alex.speed(animationSpeed)

# pre position for center polygon
alex.stamp()
alex.penup()
if circleDraw:
    alex.forward(radiusPolygon)
    alex.left(90)
    alex.pendown()
    alex.circle(radiusPolygon)
    alex.penup()
    alex.left(-90)
    alex.backward(radiusPolygon)
alex.left(half_polyAngle)
alex.backward(preMove)
alex.left(-half_polyAngle)
alex.pendown()
alex.stamp()

for angle in polyTurtleAngle:
    turtleFracLine(alex, order, size)
    alex.left(angle)
if not animation:
    myWin.tracer(True)
myWin.mainloop()
