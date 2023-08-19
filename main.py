import turtle as t
import random
# import colorgram



# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# directions = [0, 90, 180, 270]
# tim.pensize(1)
# tim.speed("fastest")


# def draw_spirograph(size_of_gap):
    
#     for _ in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)



# rgb_colors = []
# colors = colorgram.extract('image.jpg', 38)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

tim = t.Turtle()
tim.penup()
tim.hideturtle()
t.colormode(255)
tim.speed('fastest')

color_list = [(35, 28, 25), (111, 93, 83), (84, 86, 95), (169, 150, 139), (97, 85, 89), (225, 229, 238), (151, 155, 167), (87, 99, 91), (168, 150, 157), (235, 223, 216), (230, 219, 225), (58, 60, 76), (146, 160, 152), (232, 244, 237), (76, 56, 61), (83, 54, 50), (139, 130, 108), (161, 113, 104), (118, 122, 146), (182, 187, 210), (152, 113, 121), (221, 178, 170), (73, 66, 49), (208, 181, 188), (113, 137, 121), (202, 197, 170), (53, 71, 59), (169, 204, 183), (120, 131, 133), (57, 66, 69), (183, 195, 197)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)













screen = t.Screen()
screen.exitonclick()





