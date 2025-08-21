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

# screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Turtle crossing game")
screen.tracer(0)

# set up player
player = Player()

# set up cars
car = Car()

# player movement
screen.listen()
screen.onkey(player.up,"w")
screen.onkey(player.down,"s")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.05)  # delay refresh (makes game faster/slower)

    car.auto_move()
    # collision (use distance of player to distance of car to trigger collision)
    if player.distance(car.xcor(), car.ycor()) <= 0.1:
        print("hit")
        # game_is_on = False

    # trigger win
    if player.ycor() >= Y_LIMIT_UP:
        print("game won!")

# leave as last bit of code
screen.exitonclick()