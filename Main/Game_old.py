from array import array
from itertools import repeat


class GameOLd:
    def __init__(self):
        self.rolls: list = [0] * 21
        self.currentRoll: int = 0

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def score(self):
        gainedScore: int = 0
        firstBallInFrame: int = 0
        for frames in range(0, 10):
            if self.isStrike(firstBallInFrame):
                gainedScore += 10 + self.rolls[firstBallInFrame + 1] + self.rolls[firstBallInFrame + 2]
                firstBallInFrame += 1
            elif self.isSpare(firstBallInFrame):
                gainedScore += 10 + self.rolls[firstBallInFrame + 2]
                firstBallInFrame += 2
            else:
                gainedScore += self.rolls[firstBallInFrame] + self.rolls[firstBallInFrame + 1]
                firstBallInFrame += 2
        return gainedScore

    def isStrike(self, firstBallInFrame):
        if self.rolls[firstBallInFrame] == 10:
            return True

    def isSpare(self, firstBallInFrame):
        if self.rolls[firstBallInFrame] + self.rolls[firstBallInFrame + 1] == 10:
            return True
