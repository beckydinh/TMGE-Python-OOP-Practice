class Player:
    def __init__(self, name):
        self.score = 0
        self.name = name

    def incScore(self):
        self.score += 1
        