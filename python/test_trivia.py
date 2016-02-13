__author__ = 'tcw321'

import unittest
from category import *
from trivia import *

class TestTrivia(unittest.TestCase):

    def test_question_builder(self):
        category_questions = []
        game = Game()
        result = game.question_builder(category_questions, Category.Pop)
        self.assertEqual(result[0], "Pop Question 0")

    def test_rock_category_question_builder_returns_rock_question(self):
        category_questions = []
        game = Game()
        result = game.question_builder(category_questions, Category.Rock)
        self.assertEqual(result[0], "Rock Question 0")

    def test_question_builder_should_return_fifty_questions(self):
        category_questions = []
        game = Game()
        result = game.question_builder(category_questions, Category.Rock)
        self.assertEqual(len(result), 50)

class TestPlayer(unittest.TestCase):

    def test_player(self):
        players = Players()
        self.assertEqual(0, players.length())

    def test_get_players_players_length_equal_zero(self):
        players = Players()
        self.assertEqual(0, len(players.players))

if __name__ == '__main__':
    unittest.main()
