from turtle import Turtle
import random
starting_positions = [-250, -225, -200, -175, -150, -125, -100, -75, -50, -25, 0, 25, 50, 75, 100, 125, 150, 175, 200,
                      225, 250]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
speed = 5
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=300, y=random.choice(starting_positions))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(speed)

    def speed_increase(self):
        global speed
        speed += 5
        for car in self.all_cars:
            car.forward(speed)
