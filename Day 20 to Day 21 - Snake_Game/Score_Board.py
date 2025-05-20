from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

X = 0
Y = 270

class Scoreboard:
    def __init__(self, Height):
        self.score = 0
        self.high_score = 0
        self.local_turtle = self.set_up(Height)

#setup Scoreboard
    def set_up(self, Height):
        local_turtle = Turtle()
        local_turtle.penup()
        local_turtle.color("white")
        local_turtle.hideturtle()
        local_turtle.setpos(0, Height/2 - 40)
        return local_turtle

    def update_Scoreboar(self):
        with open("High Score.txt", mode="r") as f:
            self.high_score = f.read()
            self.local_turtle.clear()
            self.local_turtle.write(f"Score: {self.score} High Score: {self.high_score}", False, align="center", font = ("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1

    def reset(self):
        with open("High Score.txt", mode="r") as f:
            score = int(f.read().strip())
            print(score)
        if self.score > score:
            print("True")
            with open("High Score.txt", mode="w") as f:
                f.write(str(self.score))
        self.score = 0

    def game_over(self):
        self.local_turtle.goto(0, 0)
        self.local_turtle.write("GAME OVER", align=ALIGNMENT, font=FONT)