import unittest

from Main.game import Game


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def rollManys(self, pins, rolls):
        for i in range(rolls):
            self.g.roll(pins)

    def test_canRoll(self):
        self.g.roll(0)

    def test_guetterGame(self):
        self.rollManys(0, 20)
        self.assertEqual(0,self.g.calculateScore())

    def test_allOnes(self):
        self.rollManys(1, 20)
        self.assertEqual(20,self.g.calculateScore())


if __name__ == '__main__':
    unittest.main()
