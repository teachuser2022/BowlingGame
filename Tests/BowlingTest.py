import unittest

from Main.game import Game


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_canRoll(self):
        self.g.roll(0)

    def test_guetterGame(self):
        for i in range(20):
            self.g.roll(0)
        self.assertEqual(0,self.g.calculateScore())

if __name__ == '__main__':
    unittest.main()
