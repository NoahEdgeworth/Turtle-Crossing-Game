from turtle import Turtle

FONT = ("Courier", 24, "normal")

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful
# crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(-280, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font=("Times New Roman", 20, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=True, align="center", font=("Times New Roman", 30, "normal"))