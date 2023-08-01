from turtle import Turtle
import random


class Food(Turtle):
    """This class generates the 'food' for the snake"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest") #fastest food in the west
        self.refresh()

    def refresh(self):
        """Generates new food after it has been 'eaten' by the snake"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y= random_y)

