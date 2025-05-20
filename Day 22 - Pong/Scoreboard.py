from turtle import Turtle

class Scoreboard():

    def __init__(self, screen_height, screen_width):
        self.scorep1 = 0
        self.scorep2 = 0
        self.height = screen_height
        self.width = screen_width
        self.turtle = self.setup_turtle()

    def setup_turtle(self):
        local_turtle = Turtle()
        local_turtle.penup()
        local_turtle.color("white")
        local_turtle.hideturtle()
        local_turtle.setpos(0, self.height/2 - 140)
        return local_turtle

    def draw_score(self):
        self.turtle.clear()
        self.turtle.pendown()
        scoretring = "Score %s" % self.scorep1
        scoretring = f"{self.scorep1}   {self.scorep2}"
        self.turtle.write(scoretring, False, align="center", font = ("arial", 80, "normal"))


    def increase_scorep1(self):
        self.scorep1 += 1
        self.draw_score()


    def increase_scorep2(self):
        self.scorep2 += 1
        self.draw_score()

