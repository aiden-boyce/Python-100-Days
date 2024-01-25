from turtle import Turtle, Screen
from random import randint


def main():
    """Turtle Racing Game"""
    screen = Screen()
    screen.setup(width=500, height=400)
    race_in_progress = False

    user_bet = screen.textinput(
        title="Place your bet!",
        prompt="Which turtle will win the race?\n(Red, Orange, Yellow, Green, Blue, Indigo, Purple)\nEnter a color: ",
    ).lower()

    turtle_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
    turtle_positions = [90, 60, 30, 0, -30, -60, -90]
    turtle_list = []

    for i in range(len(turtle_colors)):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(turtle_colors[i])
        turtle.goto(-230, turtle_positions[i])
        turtle.pendown()
        turtle_list.append(turtle)

    # User placed their bet
    if user_bet:
        race_in_progress = True

    winner = ""
    # Turtle Race!
    while race_in_progress:
        for turtle in turtle_list:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)

            if turtle.xcor() > 230:
                winner = turtle.pencolor()
                race_in_progress = False
                break

    print(f"The winner is {winner.capitalize()}!!!")
    if user_bet == winner:
        print("You win!")
    else:
        print("You lost!")
    screen.exitonclick()


if __name__ == "__main__":
    main()
