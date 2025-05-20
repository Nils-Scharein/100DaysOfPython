from turtle import Turtle, Screen
import random

from Score_Board import Scoreboard
X = 100
Y = 100

screen = Screen()
apple = "apple.gif"
screen.register_shape(apple)

class Food:

    def __init__(self, Width, Height):
        self.turtle = []
        self.food = self.set_up()
        self.apple = self.turtle[0]
        self.xcor = 0
        self.ycor = 0
        self.height = Height
        self.weight = Width

    def set_up(self):
        local_turtle = Turtle()
        local_turtle.shape(apple)
        local_turtle.penup()
        self.turtle.append(local_turtle)
        return local_turtle

    def spawn_food(self):
        x = random.randrange(-((self.weight / 2) - 20), ((self.weight / 2) - 20), 20)
        y = random.randrange(-((self.height / 2) - 20), ((self.height / 2) - 20), 20)
        self.xcor = x
        self.ycor = y
        self.apple.setpos(x, y)



