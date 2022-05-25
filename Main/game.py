class Game:
    rolls: list = [0] * 20
    currentRoll = 0

    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def calculateScore(self):
        score = 0
        for i in self.rolls:
            if(self.rolls[i]+self.rolls[i+1]==10 && i%2==0):
                score+=10+self.rolls[i]
            score += self.rolls[i]
        return score
