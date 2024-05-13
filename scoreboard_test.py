from turtle import Turtle

LEVEL_SCORE = 3
DISTANCE_FOR_SCORE = 60
FONT = ("Courier", 15, "bold")
ALIGN = "center"
file_score = "score_file.txt"


class MyScreen:
    def __init__(self):
        self.y_coord = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 0
        self.high_score = 0
        self.level_speed = 0.1
        self.color("#FFFFFF")
        self.penup()
        self.hideturtle()
        self.goto(0, MyScreen().y_coord - DISTANCE_FOR_SCORE)
        self.read_scoreboard_file()
        self.refresh_score()

    def read_scoreboard_file(self):
        try:
            with open(file_score, "r") as high_score_file:
                self.high_score = int(high_score_file.read())
        except FileNotFoundError:
            self.high_score = 0

    def increase_score(self):
        self.score += 1
        self.refresh_score()
        self.increase_level()

    def increase_level(self):
        if self.score % LEVEL_SCORE == 0:
            self.level += 1
            self.level_speed *= 0.9

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file_score, "w") as high_score_file:
                high_score_file.write(str(self.score))

    def refresh_score(self):
        self.clear()
        self.write(f"Level: {self.level} Score: {self.score}\n High Score: {self.high_score}", align=ALIGN, font=FONT)


import unittest
from unittest.mock import patch


class TestScoreboard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = Scoreboard()

    def test_initial_values(self):
        self.assertEqual(self.scoreboard.score, 0)
        self.assertEqual(self.scoreboard.level, 0)
        self.assertEqual(self.scoreboard.high_score, 0)
        self.assertEqual(self.scoreboard.level_speed, 0.1)

    def test_increase_score(self):
        self.scoreboard.increase_score()
        self.assertEqual(self.scoreboard.score, 1)

    def test_increase_level(self):
        self.scoreboard.score = 2