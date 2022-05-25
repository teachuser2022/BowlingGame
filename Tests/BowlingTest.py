import unittest

from Main.game import Game


class BowlingTest(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def rollManys(self, pins, rolls):
        for i in range(rolls):
            self.g.roll(pins)


    def test_guetterGame(self):
        self.rollManys(0, 20)
        self.assertEqual(0,self.g.calculateScore())

    def test_allOnes(self):
        self.rollManys(1, 20)
        self.assertEqual(20,self.g.calculateScore())

    # @unittest.skip("reason for skipping")
    def test_oneSpare(self):
        self.g.roll(5)
        self.g.roll(5)#spare
        self.g.roll(3)
        self.rollManys(0, 17 )
        self.assertEqual(16,self.g.calculateScore())


if __name__ == '__main__':
    unittest.main()
