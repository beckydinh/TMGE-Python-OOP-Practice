from Player import Player

class Controller:
    def __init__(self):
        self.players = []
        self.currPlayer = ""
        self.player2 = ""

    def createProfile(self, name):
        if not self.playerNameExists(name):
            self.players.append(Player(name))

    def loginCurrPlayer(self, name):
        if self.playerNameExists(name):
            self.currPlayer = name
    
    def loginPlayer2(self, name):
        if self.playerNameExists(name):
            self.player2 = name

    def playerNameExists(self, name):
        for p in self.players:
            if p.name == name:
                return True
        return False

    def printPlayers(self):
        for p in self.players:
            print(p.name)

    def printPlayersExcept(self, name):
        for p in self.players:
            if p.name != name:
                print(p.name)
    
    def incrPlayerScore(self, name):
        for p in self.players:
            if p.name == name:
                p.incScore()
                break

    def getUserScore(self, name):
        for p in self.players:
            if p.name == name:
                return p.score
        return -1

    def getTotalPlayers(self):
        return len(self.players)