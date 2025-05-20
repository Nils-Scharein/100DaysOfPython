import random
from turtle import Screen, Turtle
from Cars import Car
from Player import Player
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

HEIGHT = 600
WIDTH = 600

LANES = list(range(int(-(HEIGHT / 2)), int((HEIGHT / 2)) + 20, 20))

screen = Screen()
screen.setup(HEIGHT, WIDTH)
screen.tracer(0)

player = Player()
roadslen = []
lt_lanes = []
lt_cars_dic = {}
lt_cars = []
rt_lanes = []
rt_cars_dic = {}
rt_cars = []
cars = []


# create sprites of the roads
def roads():
    road = Turtle()
    road.penup()
    road.setpos(WIDTH / 2, HEIGHT / 2)
    road.setheading(LEFT)
    step = HEIGHT / 2
    distance = 5
    for i in range(HEIGHT // 20):
        for i in range(WIDTH // distance):
            road.pendown()
            road.fd(distance)
            road.penup()
            road.fd(distance)
        step -= 20
        road.setpos(WIDTH / 2, step)
        roadslen.append(1)


def random_lanes():
    for i in LANES:
        a = random.randint(0, 1)
        if a == 1:
            rt_lanes.append(i)
            rt_cars_dic[i] = []
        if a == 0:
            lt_lanes.append(i)
            lt_cars_dic[i] = []
    print(f"left Lanes: {lt_lanes}")
    print(f"right Lanes: {rt_lanes}")
    print(f"all Lanes: {LANES}")

# check spawn of cars
def spawn():
    for i in rt_lanes:
        a = random.randint(0, 5)
        if a == 1:
            car = Car(HEIGHT, WIDTH)
            car.setheading(RIGHT)
            car.setpos(-(WIDTH / 2), i)
            rt_cars.append(car)
            if rt_cars_dic[i] != []:
                car.speed = rt_cars_dic[i][-1].speed
                if car.distance(rt_cars_dic[i][-1].pos()) < 40:
                    car.setpos(car.xcor() + 40, car.ycor())
                car.setpos(-300, car.ycor())
            rt_cars_dic[i].append(car)
            cars.append(car)
    for i in lt_lanes:
        b = random.randint(0, 5)
        if b == 1:
            car = Car(HEIGHT, WIDTH)
            car.setheading(LEFT)
            car.setpos(WIDTH / 2, i)
            lt_cars.append(car)
            if lt_cars_dic[i] != []:
                car.speed = lt_cars_dic[i][-1].speed
                if car.distance(lt_cars_dic[i][-1].pos()) < 40:
                    car.setpos(car.xcor() - 40, car.ycor())
            lt_cars_dic[i].append(car)
            cars.append(car)

def move_all():
    for car in lt_cars:
        car.move()
    for car in rt_cars:
        car.move()


def main():
    game_on = True
    roads()
    random_lanes()
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")
    while game_on:
        if random.randint(0, 14) == 1:
            spawn()
        move_all()
        if player.colision(cars) or player.win():
            game_on = False
        screen.update()
        time.sleep(0.02)


screen.listen()
main()
screen.exitonclick()
