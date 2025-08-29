from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,240)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() # clear previous text otherwise will slow down game a LOT
        self.write(f"Your score: {int(self.player_score)}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"Game over! \nYour final score: {int(self.player_score)}", align=ALIGNMENT, font=FONT)