# import colorgram
#
# colors = colorgram.extract('image.jpg', 100)
# print (colors)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen
import random

colors = [(103, 162, 221), (45, 98, 170), (157, 92, 23), (63, 130, 205), (47, 26, 5), (228, 150, 63), (186, 151, 25), (183, 207, 231), (12, 63, 138), (93, 86, 7), (6, 23, 4), (159, 193, 228), (171, 149, 169), (244, 208, 77), (246, 231, 213), (3, 17, 43), (229, 211, 220), (17, 4, 9), (126, 43, 11), (211, 104, 52), (125, 104, 128), (139, 118, 143), (34, 92, 12), (207, 182, 196), (217, 209, 21), (62, 117, 42), (215, 181, 174), (233, 243, 236), (92, 159, 64), (121, 172, 111), (106, 38, 44), (166, 199, 215), (167, 213, 135), (36, 72, 86), (110, 135, 142)]

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.penup()


x = -250
y = -250

tim.setpos(x, y)


for _ in range(10):
    for _ in range(10):
        color = random.choice(colors)
        tim.dot(20, color)
        tim.fd(50)
    y +=50
    tim.setpos(x, y)














screen.exitonclick()