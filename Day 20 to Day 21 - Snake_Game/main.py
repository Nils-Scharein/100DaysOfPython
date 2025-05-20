from turtle import Screen
from Snake import Snake
from Score_Board import Scoreboard
from Food import Food
import time

WIDTH = 600
HEIGHT = 600

#setup screen origin
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake(WIDTH, HEIGHT)
score = Scoreboard(HEIGHT)
food = Food(WIDTH, HEIGHT)


#Globale Variablen, Liste, etc.
sleep = 0.05
food.spawn_food()

#Snakebody aufteilen


def set_heading():
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.up, "Up")

def main():
    is_game_on = True
    set_heading()
    food.spawn_food()
    snake.change_sprites()
    food.spawn_food()

    while is_game_on:
        time.sleep(sleep)
        screen.update()
        snake.move()
        snake.change_sprites()
        score.update_Scoreboar()
        snake.eat(food, score)
        if snake.check_colison():
            score.reset()
            snake.reset()






screen.listen()
main()

screen.exitonclick()