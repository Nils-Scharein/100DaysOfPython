from turtle import Turtle, Screen, Shape
import time
from playsound import playsound
from PIL import Image, ImageTk
from itertools import product

screen = Screen()

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
TILE = 16

PARTS = ["head_up", "head_right", "head_down", "head_left", "tail_up", "tail_right", "tail_down", "tail_left", "curve1", "curve2", "curve3", "curve4", "straight_up_down" ,"straight_left_right", "bunny", "grass"]
snakebody = []


def tile(d):
    #name, ext = os.path.splitext(filename)
    img = Image.open("Snakebody.gif")
    w, h = img.size
    grid = product(range(0, h - h % d, d), range(0, w - w % d, d))
    for i, j in grid:
        box = (j, i, j + d, i + d)
        snakebody.append(img.crop(box))
tile(TILE)
#snakebody[8].show()
#snakebody[9].show()
#snakebody[10].show()
#snakebody[11].show()

def register_PIL(name, image):
    photo_image = ImageTk.PhotoImage(image)
    shape = Shape("image", photo_image)
    screen._shapes[name] = shape  # underpinning, not published API

for i in range(0, len(PARTS)):
    register_PIL(PARTS[i], snakebody[i])

def function_sound():
    playsound("audio.wav", False)

class Snake:
    def __init__(self, Width, Height):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.height = Height
        self.width = Width

    def create_snake(self):
        for position in STARTING_POS:
            new = Turtle()
            new.color("white")
            new.shape("square")
            new.penup()
            new.goto(position)
            self.segments.append(new)

    def new_tail(self):
        x, y = self.segments[-1].pos()
        new = Turtle()
        new.color("white")
        new.shape("square")
        new.penup()
        new.goto(x, y)
        self.segments.append(new)

    def check_colison(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment.pos()) < 19:
                return True
        if self.head.xcor() > (self.width/2) - 10 or self.head.xcor() < -(self.width/2) - 10:
            return True
        if self.head.ycor() > (self.height/2) - 10 or self.head.ycor() < -(self.height/2) - 10:
            return True

    def eat(self, food, scoreboard):
        if self.head.distance(food.apple.pos()) <= 19:
            a = True
            ziel = len(self.segments)
            while a:
                counter = 0
                food.spawn_food()
                for segment in self.segments:
                    if segment.distance(food.xcor, food.ycor) >= 19:
                        counter += 1
                if counter == ziel:
                    food.apple.setpos(food.xcor, food.ycor)
                    scoreboard.increase_score()
                    self.new_tail()
                    function_sound()
                    a = False

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            heading = self.segments[seg_num - 1].heading()
            self.segments[seg_num].setpos(new_x, new_y)
            self.segments[seg_num].setheading(heading)
        self.head.fd(MOVE_DISTANCE)


    def change_sprites(self):
        for seg_num in range(len(self.segments) - 1):
            #head check
            if self.segments[0].heading() == LEFT:
                self.segments[0].shape("head_left")
            elif self.segments[0].heading() == RIGHT:
                self.segments[0].shape("head_right")
            elif self.segments[0].heading() == UP:
                self.segments[0].shape("head_up")
            elif self.segments[0].heading() == DOWN:
                self.segments[0].shape("head_down")
            #tail check
            if self.segments[-1].heading() == LEFT:
                self.segments[-1].shape("tail_left")
            elif self.segments[-1].heading() == RIGHT:
                self.segments[-1].shape("tail_right")
            elif self.segments[-1].heading() == UP:
                self.segments[-1].shape("tail_up")
            elif self.segments[-1].heading() == DOWN:
                self.segments[-1].shape("tail_down")

            #check gerade
            if self.segments[seg_num].heading() == self.segments[seg_num + 1].heading() and self.segments[seg_num].heading() == UP or self.segments[seg_num].heading() == DOWN:
                self.segments[seg_num].shape("straight_up_down")
            if self.segments[seg_num].heading() == self.segments[seg_num + 1].heading() and self.segments[seg_num].heading() == LEFT or self.segments[seg_num].heading() == RIGHT:
                self.segments[seg_num].shape("straight_left_right")

            #curven
            if self.segments[seg_num].heading() == RIGHT and self.segments[seg_num + 1].heading() == DOWN or self.segments[seg_num].heading() == UP and self.segments[seg_num + 1].heading() == LEFT:
                self.segments[seg_num].shape("curve1")
            elif self.segments[seg_num].heading() == UP and self.segments[seg_num + 1].heading() == RIGHT or self.segments[seg_num].heading() == LEFT and self.segments[seg_num + 1].heading() == DOWN:
                self.segments[seg_num].shape("curve4")
            elif self.segments[seg_num].heading() == RIGHT and self.segments[seg_num + 1].heading() == UP or self.segments[seg_num].heading() == DOWN and self.segments[seg_num + 1].heading() == LEFT:
                self.segments[seg_num].shape("curve2")
            elif self.segments[seg_num].heading() == LEFT and self.segments[seg_num + 1].heading() == UP or self.segments[seg_num].heading() == DOWN and self.segments[seg_num + 1].heading() == RIGHT:
                self.segments[seg_num].shape("curve3")

    def reset(self):
        for segment in self.segments:
            segment.setpos(999999,9999999)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            time.sleep(0.01)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            time.sleep(0.01)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            time.sleep(0.01)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            time.sleep(0.01)