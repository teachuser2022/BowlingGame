class Game:
    rolls: list = [0] * 20
    currentRoll = 0

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def calculateScore(self):
        score = 0
        for pinInRoll in self.rolls:
            score += pinInRoll
        return score
