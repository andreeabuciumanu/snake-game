from turtle import Turtle

SCORE = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.actual_score(SCORE)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", move=False, align="center", font=("Arial", 12, "normal"))

    def actual_score(self, score):
        self.clear()
        self.write(f'Score: {score}', move=False, align="center", font=("Arial", 12, "normal"))
