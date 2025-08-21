from turtle import Turtle
from constants import RIGHT, LEFT, MOVING_INCREMENTS, X_LIMIT_LEFT, X_LIMIT_RIGHT, SCREEN_HEIGHT, Y_LIMIT_DOWN, Y_LIMIT_UP
import random

class Car(Turtle):

    # set up cars in a row
    # no_of_cars = (SCREEN_HEIGHT - 3 * MOVING_INCREMENTS) / MOVING_INCREMENTS # integer
    # positions = list(range(Y_LIMIT_DOWN + MOVING_INCREMENTS, Y_LIMIT_UP, MOVING_INCREMENTS))  # [-260 to 260] list
    # car_list = []

    def __init__(self):
        super().__init__() # for Player class to inherit Turtle's attributes
        self.setheading(LEFT)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=1.5)

    def auto_move(self): # cars to auto-move and then re-appear on right side when left wall is reached
        if self.xcor() > X_LIMIT_LEFT:
            self.forward(MOVING_INCREMENTS)
        if self.xcor() == X_LIMIT_LEFT:
            self.goto(280,self.ycor()) #TODO: FLAGGED FOR CHANGE - 280 TO CHANGE TO RANDOM_X

    # def auto_lineup(self):
    #     positions = list(range(Y_LIMIT_DOWN + MOVING_INCREMENTS, Y_LIMIT_UP, MOVING_INCREMENTS))  # [-260 to 260] list
    #     random_x = random.randint(450,900)
    #     car_list = []
    #     # create grid
    #     for position in positions:
    #         car = Car()
    #         car_list.append(car)
    #         car.goto(random_x, position)
