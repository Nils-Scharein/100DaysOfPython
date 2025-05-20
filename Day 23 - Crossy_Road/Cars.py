from turtle import Turtle
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

colors = ["red"]
speed = [3, 4, 5, 6, 7, 8, 9, 10]

class Car(Turtle):

    def __init__(self, HEIGHT, WIDTH):
        super().__init__()
        self.WIDTH = WIDTH
        self.HIGHT = HEIGHT
        #setup Turtle
        self.penup()
        self.color(random.choice(colors))
        self.shape("square")
        self.speed = random.choice(speed)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x = 0
        self.y = 0
        self.setpos(self.x, self.y)


    def set_y(self):
        pass

    def move(self):
        self.fd(self.speed)

