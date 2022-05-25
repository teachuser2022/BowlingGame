class Game:
    __score = 0

    def roll(self, pins):
        self.__score+=pins

    def calculateScore(self):
        return self.__score
