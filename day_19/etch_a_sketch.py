from turtle import Turtle, Screen

TURTLE = Turtle()


def move_forward():
    TURTLE.forward(10)


def move_backward():
    TURTLE.backward(10)


def turn_right():
    new_heading = TURTLE.heading() - 10
    TURTLE.setheading(new_heading)


def turn_left():
    new_heading = TURTLE.heading() + 10
    TURTLE.setheading(new_heading)


def clear_board():
    TURTLE.clear()
    TURTLE.penup()
    TURTLE.home()
    TURTLE.pendown()


def main():
    """Etch A Sketch Game"""
    screen = Screen()
    screen.listen()
    screen.onkey(move_forward, "w")
    screen.onkey(move_backward, "s")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(clear_board, "c")
    screen.exitonclick()


if __name__ == "__main__":
    main()
