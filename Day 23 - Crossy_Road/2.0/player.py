from turtle import Turtle
STARTING_POSITION = (0, -280)
FINISH_LINE_Y = 280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Player(Turtle):
    def __init__(self, MOVE_DISTANCE):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(UP)
        self.penup()
        self.setpos(STARTING_POSITION)
        self.MOVE_DISTANCE = MOVE_DISTANCE

    def move_up(self):
        self.fd(self.MOVE_DISTANCE)

    def move_down(self):
        self.bk(self.MOVE_DISTANCE)

    def check_colision_car(self, cars):
        for car in cars:
            if car.distance(self.pos()) < 20:
                return True

    def check_colision_finish(self, scoreboard, car_manager):
        if self.ycor() >= FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
            scoreboard.increase_level()
            car_manager.increase_movement()

