__author__ = 'tcw321'

from trivia import *

not_a_winner = False

game = Game()

game.add('Chet')
game.add('Pat')
game.add('Sue')

for i in range(5):
    game.roll(i)

    for v in [7, 8]:
        if v == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

    if not not_a_winner: break