from Board import Board
from Connect4State import Connect4State

class Connect4Board(Board):
    def __init__(self, height, width, totalPlayers):
        super().__init__(height, width, totalPlayers)
        self.connect4GameState = Connect4State(totalPlayers)

    def drop(self, value, col):
        super().updateBoard(value, self.getBottomEmptyRow(col), col)

    def checkWin(self):
        return self.connect4GameState.checkWin(self)

    def getBottomEmptyRow(self, col):
        totalRows = self.height
        board = self.boardArray
        for row in range(totalRows - 1, -1, -1):
            if board[row][col] == None:
                return row
        return -1
    
