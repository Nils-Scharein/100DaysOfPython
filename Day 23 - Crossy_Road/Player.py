from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(UP)
        self.penup()
        self.setpos(0, -280)

    def move_up(self):
        self.fd(20)

    def move_down(self):
        self.bk(20)

    def colision(self, cars):
        for car in cars:
            if car.distance(self.pos()) < 20:
                return True

    def win(self):
        if self.ycor() > 240:
            print("You Win")
            return True