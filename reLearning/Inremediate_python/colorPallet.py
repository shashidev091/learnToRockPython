import random
import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('hist.jpeg', 30)

#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)

colors_list = [(250, 246, 243), (248, 245, 246), (211, 154, 98), (53, 107, 131), (242, 249, 246), (235, 240, 244),
               (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130),
               (190, 88, 109), (12, 50, 64), (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143),
               (166, 21, 30), (224, 93, 79), (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22),
               (21, 78, 90), (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210)]


my_turtle = Turtle()
# my_turtle.pensize(30)
my_screen = Screen()
my_screen.colormode(255)

# for _ in range(10):
#     my_turtle.color(random.choice(colors_list))
#     my_turtle.forward(50)
#     my_turtle.right(random.choice([0, 90, 180, 270]))

my_turtle.setheading(255)
my_turtle.forward(300)
my_turtle.setheading(0)

for dot_count in range(1, 101):
    my_turtle.dot(20, random.choice(colors_list))
    my_turtle.forward(50)

    if dot_count % 10 == 0:
        my_turtle.setheading(90)
        my_turtle.forward(50)
        my_turtle.setheading(180)
        my_turtle.forward(500)
        my_turtle.setheading(0)

my_screen.exitonclick()
