from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.setpos(-220, 260)
        self.hideturtle()

    def draw_score(self):
        self.clear()
        self.pendown()
        scoretring = "Level: " + str(self.level)
        self.write(scoretring, False, align="center", font = (FONT))

    def increase_level(self):
        self.level += 1
        self.draw_score()

    def lose(self):
        self.clear()
        self.penup()
        self.setpos(0, 0)
        self.pendown()
        scoretring = "You Lose!"
        self.write(scoretring, False, align="center", font=(FONT))
