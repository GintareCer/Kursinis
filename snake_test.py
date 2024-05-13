import unittest
from unittest.mock import MagicMock
from snake import Snake, starting_position, STEP_TO_MOVE, RIGHT

class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_create_snake(self):
        self.assertEqual(len(self.snake.list_of_piece), len(starting_position))
        for i, position in enumerate(starting_position):
            self.assertEqual(self.snake.list_of_piece[i].position(), position)

    def test_add_tail(self):
        initial_length = len(self.snake.list_of_piece)
        self.snake.add_tail((10, 10))
        self.assertEqual(len(self.snake.list_of_piece), initial_length + 1)
        self.assertEqual(self.snake.list_of_piece[-1].position(), (10, 10))

    def test_reset_snake(self):
        initial_length = len(self.snake.list_of_piece)
        self.snake.reset_snake()
        self.assertEqual(len(self.snake.list_of_piece), initial_length)

    def test_move_snake(self):
        self.snake.head.forward = MagicMock()
        self.snake.move_snake()
        self.snake.head.forward.assert_called_once_with(STEP_TO_MOVE)

    def test_snake_right(self):
        self.snake.head.setheading = MagicMock()
        self.snake.snake_right()
        self.snake.head.setheading.assert_called_once_with(RIGHT)

if __name__ == '__main__':
    unittest.main()