import unittest

from Main.game import Game


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_canRoll(self):
        self.g.roll(0)


if __name__ == '__main__':
    unittest.main()
