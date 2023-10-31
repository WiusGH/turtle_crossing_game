from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-260, y=260)
        self.write(f'level: {self.level}', font=FONT)

    def next_level(self):
        self.level += 1
        self.goto(x=-260, y=260)
        self.clear()
        self.write(f'level: {self.level}', font=FONT)

    def game_over(self):
        self.goto(-90, 0)
        self.write('You lose!', font=FONT)
