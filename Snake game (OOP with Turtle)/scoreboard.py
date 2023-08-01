from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Score(Turtle):
    """This class keeps track of the current score, updates the scoreboard and resets itself in case of game-over.
    It also detects if there is a new high score, and writes the new high score to the 'high score' file."""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.highscore = int(data.read())
        self.setpos(x=0, y=280)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def keep_score(self):
        """Keeps track of the score and calls the update-scoreboard method."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        """Checks if final score is higher than current highscore, and if yes, overwrites the 'highscore' file with the new highscore, in case of game-over."""
        if self.score > self.highscore:
            self.highscore = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

