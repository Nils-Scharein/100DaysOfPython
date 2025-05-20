import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

Movement = 20
WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player(Movement)
car_manager = CarManager()

def main():
    game_is_on = True
    car_manager.roads(WIDTH, HEIGHT, Movement)
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")
    scoreboard.draw_score()
    while game_is_on:
        car_manager.move_all()
        if random.randint(0, 6) == 0:
            car_manager.spawn(WIDTH)
        if player.check_colision_car(car_manager.cars):
            scoreboard.lose()
            game_is_on = False
        player.check_colision_finish(scoreboard, car_manager)
        time.sleep(0.1)
        screen.update()

screen.listen()
main()
screen.exitonclick()