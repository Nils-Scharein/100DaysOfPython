from turtle import Turtle
import random
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball(Turtle):

    def __init__(self, HEIGHT, WIDTH):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.height = HEIGHT
        self.width = WIDTH
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.02

    def move(self, SPEED):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.movespeed *= 0.7

    def score_goal(self, Scoreboard):
        if self.xcor() < -(self.width/2) + 20:
            Scoreboard.increase_scorep2()
            self.setpos(0, 0)
            self.movespeed = 0.05
        elif self.xcor() > (self.width/2) - 20:
            Scoreboard.increase_scorep1()
            self.setpos(0, 0)
            self.movespeed = 0.05
        else:
            pass