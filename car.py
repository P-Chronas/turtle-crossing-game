from turtle import Turtle
from constants import RIGHT, LEFT, MOVING_INCREMENTS, X_LIMIT_LEFT, X_LIMIT_RIGHT, SCREEN_HEIGHT, Y_LIMIT_DOWN, Y_LIMIT_UP
import random

class Car(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__() # for Player class to inherit Turtle's attributes
        self.setheading(LEFT)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=None, stretch_len=1.5)
        self.goto(x_pos,y_pos)

    def auto_move(self): # cars to auto-move and then re-appear on right side when left wall is reached
        if self.xcor() > X_LIMIT_LEFT-40: # -40 to allow cars to move past left wall before disappearing
            self.forward(MOVING_INCREMENTS/4)
        else:
            self.goto(-self.xcor() + 20, self.ycor())