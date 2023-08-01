import random
from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
colour_options = ["blue", "red", "purple", "orange", "green", "yellow", "pink", "magenta", "maroon", "navy", "salmon",
                  "SandyBrown", "SeaGreen", "sienna", "tomato", "tan", "gold", "firebrick", "honeydew", "khaki",
                  "brown", "azure", "white"]


class Snake:
    """This class creates the snake, updates the snake length and sets controls for the snake's movements."""
    def __init__(self):
        self.segments = []
        self.x_axis = 0
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Makes the blocks of the snake follow the path of the block in the front"""
        for block_num in range((len(self.segments)-1), 0, -1):
            new_x = self.segments[block_num-1].xcor()
            new_y = self.segments[block_num-1].ycor()
            self.segments[block_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        """Creates the snake at the starting position."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Extends the snake with 1 segment, using a randomly selected colour."""
        new_block = Turtle(shape="square")
        new_block.color(random.choice(colour_options))
        new_block.penup()
        new_block.goto(position)
        self.segments.append(new_block)

    def reset(self):
        """Resets the amount of segments in the snake and calls the create_snake method"""
        for segment in self.segments:
            segment.reset()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Calls the add_segment method and assigns the position as the last segment in the line."""
        self.add_segment(self.segments[-1].position())

    def up(self):
        """Allows the snake to move up, but only if the snake is not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            None

    def down(self):
        """Allows the snake to move down, but only if the snake is not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            None

    def left(self):
        """Allows the snake to move left, but only if the snake is not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            None

    def right(self):
        """Allows the snake to move right, but only if the snake is not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            None



