import unittest

from Main.game import Game


class BowlingTest(unittest.TestCase):
    def test_canCreateGmae(self):
        g = Game()
    def test_canRoll(self):
        g=Game()
        g.roll(0)

if __name__ == '__main__':
    unittest.main()
