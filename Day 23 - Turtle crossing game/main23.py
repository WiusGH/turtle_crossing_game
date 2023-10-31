import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Screen related
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
# Player related
wius = Player()
# Scoreboard relates
scoreboard = Scoreboard()
# Keypress related
screen.onkeypress(wius.move, 'w')
# Cars related
cars = CarManager()
# Game functions
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    if wius.ycor() > 280:
        scoreboard.next_level()
        wius.goto(0, -280)
        cars.speed_increase()
    for car in cars.all_cars:
        if wius.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
