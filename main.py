"""
TURTLE CROSSING GAME, developed by Peter Chronas

default turtle size is ~20x20 pixels

screen size: 600x600px
"""

from turtle import Screen
from player import Player
from car import Car
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, MOVING_INCREMENTS, Y_LIMIT_DOWN, Y_LIMIT_UP, X_LIMIT_RIGHT, X_LIMIT_LEFT
import time
import random

from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle crossing game")
screen.tracer(0)

# set up player
player = Player()

# player movement
screen.listen()
screen.onkey(player.up,"w")
screen.onkey(player.down,"s")

# set up scoreboard
scoreboard = Scoreboard()

speed_factor = 4
next_round = True

while next_round:

    current_round = True
    win_detected = False

    # set up cars
    y_positions = list(range(Y_LIMIT_DOWN + MOVING_INCREMENTS, Y_LIMIT_UP, MOVING_INCREMENTS))
    random_no = range(300, 900, 5)
    colour_list = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "gray", "black"]
    car_list = []
    for y in y_positions:
        random_x = random.choice(random_no)
        random_colour = random.choice(colour_list)
        car = Car(random_x, y)
        car.color(random_colour)
        car_list.append(car)
    # --------------------

    while current_round:

        screen.update()
        time.sleep(0.05)

        for car in car_list:
            car.auto_move(speed_factor)

            if player.distance(car.xcor(), car.ycor()) <= 15:
                print("You have been hit by a car.")
                current_round = False
                next_round = False
                break

        if player.ycor() >= Y_LIMIT_UP:
            print("Game won!")
            win_detected = True
            current_round = False
            scoreboard.player_score += 1
            scoreboard.update_scoreboard()

    # round teardown
    if win_detected:
        for c in car_list:   # hide all cars
            c.hideturtle()
        screen.update()      # force redraw
        player.goto(0, -280)
        speed_factor = speed_factor * 0.95 # difficulty goes up each round


# leave as last bit of code
screen.exitonclick()