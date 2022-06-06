import colorgram
import turtle as turtle_module
from random import *
colors = colorgram.extract('hirst.jpg', 20)
#colorgram.extract returns Color objects, which let you access RGB, HSL, and what
#proportion of the image was that color.

tim = turtle_module.Turtle()
screen = turtle_module.Screen()
#A module has classes to create different instance objects.
turtle_module.colormode(255)

rgb_colors = []

for color in colors:
    #So, it returns Color objects. So "color" in the for loop turns to an object and that's why
    #you can access the tuple "rgb" and then the variable "r, g, or b"
    r = color.rgb.r
    #.rgb. is a tuple of RGB and to access the first value of that tuple you use .r or [0]
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tim.speed(0)
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, choice(rgb_colors))
        tim.forward(50)
        tim.hideturtle()

    tim.backward(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

screen.exitonclick()
