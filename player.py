from turtle import Turtle
from constants import UP, DOWN, MOVING_INCREMENTS, Y_LIMIT_DOWN, Y_LIMIT_UP

class Player(Turtle):

    def __init__(self):
        super().__init__() # for Player class to inherit Turtle's attributes
        self.setheading(UP)
        self.penup()
        self.shape("turtle")
        self.goto(0,-280)

    def up(self):
        if self.ycor() >= Y_LIMIT_UP: # stop movement when at border
            pass
        else:
            self.forward(MOVING_INCREMENTS)

    def down(self):
        if self.ycor() <= Y_LIMIT_DOWN:
            pass
        else:
            self.backward(MOVING_INCREMENTS)