import unittest
from unittest.mock import MagicMock
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from display import MyScreen
from bord import BordGame
import time

class TestSnake(unittest.TestCase):
    def test_move_snake(self):
        pass 

    def test_reset_snake(self):
        pass

class TestFood(unittest.TestCase):
    def test_random_food(self):
        pass

class TestScoreboard(unittest.TestCase):
    def test_increase_score(self):
        pass

class TestMyScreen(unittest.TestCase):
    def test_listen_snake(self):
        pass

class TestBordGame(unittest.TestCase):
    def test_create_bord(self):
        pass

if __name__ == '__main__':
    unittest.main()