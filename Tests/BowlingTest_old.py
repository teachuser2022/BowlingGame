# import unittest
#
# from Main.Game import Game
#
#
# class BowlingTestoLD(unittest.TestCase):
#     def setUp(self):
#         self.g = Game()
#
#     def rollMany(self, pin, rolls):
#         for i in range(0, rolls):
#             self.g.roll(pin)
#
#     def spareRoll(self):
#         self.g.roll(5)
#         self.g.roll(5)
#
#     def strikeRoll(self):
#         self.g.roll(10)
#
#     def test_gutterGame(self):
#         self.rollMany(0, 20)
#         self.assertEqual(self.g.score(), 0)
#
#     def test_allOnes(self):
#         self.rollMany(1, 20)
#         self.assertEqual(self.g.score(), 20)
#
#     # @unittest.skip("reason for skipping")
#     def test_onsSpare(self):
#         self.spareRoll()
#         self.g.roll(3)
#         self.rollMany(17, 0)
#         self.assertEqual(16, self.g.score())
#
#     def test_oneStrike(self):
#         self.strikeRoll()
#         self.g.roll(3)
#         self.g.roll(4)
#         self.rollMany(16, 0)
#         self.assertEqual(24, self.g.score())
#
#
#
#     # ----------------------------------------------------------------------
#
#
# if __name__ == '__main__':
#     unittest.main()
