from State import State
from Tile import Tile

class Board:
    def __init__(self, height, width, totalPlayers):
        self.height = height
        self.width = width
        self.boardArray = []
        for row in range(height):
            currRow = []
            for col in range(width):
                currRow.append(None)
            self.boardArray.append(currRow)
        self.gameState = State(totalPlayers)

    def isValidColumn(self, col):
        return 0 <= col < self.width

    def isValidRow(self, row):
        return 0 <= row < self.height

    def updateBoard(self, value, row, col):
        if self.isValidRow(row) and self.isValidColumn(col) and\
           self.boardArray[row][col] == None:
           self.boardArray[row][col] = Tile(value, row, col)
           self.gameState.nextTurn()

    def checkWin(self):
        return self.gameState.checkWin(self)

    def nextTurn(self):
        self.gameState.nextTurn()

    def getTurn(self):
        return self.gameState.getTurn()

    def printBoard(self):
        for row in range(self.height):
            for col in range(self.width):
                currTile = self.boardArray[row][col]
                if currTile == None:
                    print(" . ", end="")
                else:
                    print(" " + str(currTile.value) + " ", end="")
            print()
        for i in range(self.width):
            print(" " + str(i + 1) + " ", end="")
        print()
    
    def getBoard(self):
        return self.boardArray