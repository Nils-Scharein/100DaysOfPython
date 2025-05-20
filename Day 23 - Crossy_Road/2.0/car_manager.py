from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
roads = []

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.movedistance = STARTING_MOVE_DISTANCE
        self.penup()
        self.color(random.choice(COLORS))
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x = 0
        self.y = 0
        self.setpos(self.x, self.y)
        self.cars = []

    def increase_movement(self):
        self.movedistance += MOVE_INCREMENT

    def spawn(self, WIDTH):
        for lane in roads:
            if random.randint(0, 10) == 0:
                car = CarManager()
                car.showturtle()
                car.setheading(LEFT)
                car.setx(WIDTH / 2)
                car.sety(lane)
                self.cars.append(car)

    def move_all(self):
        for car in self.cars:
            car.fd(self.movedistance)

    def roads(self, WIDTH, HEIGHT, Movement):
        road = Turtle()
        road.penup()
        road.hideturtle()
        road.setpos(WIDTH / 2, HEIGHT / 2)
        road.setheading(LEFT)
        step = HEIGHT / 2
        distance = Movement
        for i in range((HEIGHT - 40) // Movement):
            for i in range(int((WIDTH / 2)) // distance):
                road.pendown()
                road.fd(distance)
                road.penup()
                road.fd(distance)
            roads.append(round(road.ycor()))
            step -= Movement
            road.setpos(WIDTH / 2, step)