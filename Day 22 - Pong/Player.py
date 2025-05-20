from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
Distance = 80


class Player(Turtle):

    def __init__(self, Height, Width, start, WID):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(WID, stretch_len=1)
        self.penup()
        self.setpos(start)
        self.height = Height
        self.width = Width

    def up(self):
        if self.ycor() < self.height/2 - 20:
            new_y = self.ycor() + Distance
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > (-self.height / 2) + 180:
            new_y = self.ycor() - Distance
            self.goto(self.xcor(), new_y)

