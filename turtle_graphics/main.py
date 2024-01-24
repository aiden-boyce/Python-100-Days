# Day 18
# Turtle, Screen, Color Mode
import turtle
from random import choice, randint
import colorgram


def get_random_color():
    """Get a random RGB value"""
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)


def draw_dashed_line(turtle):
    for i in range(30):
        if i % 2 == 0:
            turtle.pendown()
        else:
            turtle.penup()
        turtle.forward(10)


def draw_shape(turtle, num_sides):
    """Draw any equilateral shape with n sides"""
    angle = 360.0 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.left(angle)


def draw_up_to_n_sided_shape(turtle, num_sides):
    """Draw Triangle to n-sided Shapes"""
    for num_sides in range(3, num_sides + 1):
        rand_color = get_random_color()
        turtle.color(rand_color)
        draw_shape(turtle, num_sides)


def draw_random_walk(turtle, num_draws):
    """Draw a random walk"""
    directions = [0, 90, 180, 270]
    for _ in range(num_draws):
        rand_color = get_random_color()
        turtle.color(rand_color)
        direction = choice(directions)
        turtle.setheading(direction)
        turtle.forward(25)


def draw_spirograph(turtle, size_of_gap):
    """Draw a spirograph"""
    for _ in range(360 // size_of_gap):
        rand_color = get_random_color()
        turtle.color(rand_color)
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


def get_colors_from_image(image, num_colors):
    """Get the color list from an image"""
    colors = colorgram.extract(image, num_colors)
    rgb_colors = []
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        rgb = (red, green, blue)
        rgb_colors.append(rgb)
    # Remove the white background colors
    rgb_colors = rgb_colors[2:]
    return rgb_colors


def draw_m_x_n_spot_painting(turtle, colors, width, height):
    "Draw a m by n spot painting"
    turtle.penup()
    turtle.setheading(225)
    turtle.forward(300)
    pos_zero = width * 50
    for _ in range(height):
        for _ in range(width):
            color = choice(colors)
            turtle.color(color)
            turtle.setheading(0)
            turtle.dot(20)
            turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(pos_zero)
        turtle.setheading(90)
        turtle.forward(50)


def main():
    timmy = turtle.Turtle()
    turtle.colormode(255)
    timmy.shape("turtle")
    timmy.pensize(2)
    timmy.speed("fastest")
    # draw_up_to_n_sided_shape(timmy, 10)
    # draw_random_walk(timmy, 300)
    # draw_spirograph(timmy, 5)
    rgb_colors = get_colors_from_image("spot_painting.jpg", 30)
    draw_m_x_n_spot_painting(timmy, rgb_colors, 10, 10)
    screen = turtle.Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
