from turtle import Turtle

FONT = ("Courier", 10, "normal")

class StateName(Turtle):
    def __init__(self, state_name, x_cor, y_cor):
        super().__init__()
        self.state_name = state_name
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.hideturtle()
        self.penup()
        self.goto((self.x_cor, self.y_cor))
        self.write(f"{self.state_name}", align="center", font=FONT)