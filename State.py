class State:
    def __init__(self, totalPlayers):
        self.turn = 1
        self.totalPlayers = totalPlayers

    def nextTurn(self):
        self.turn += 1
        if self.turn > self.totalPlayers:
            self.turn = 1
        return self.turn

    def getTurn(self):
        return self.turn

    def checkWin(self, board):
        boardArray = board.boardArray
        for row in range(len(boardArray)):
            for col in range(len(boardArray[row])):
                if self.isWinningSequence(board, row, col):
                    return True
        return False

    # override
    def isWinningSequence(self, board, row, col):
        return self.winningSequenceDirection(board, row, col, 0, 1) or\
               self.winningSequenceDirection(board, row, col, 0,-1) or\
               self.winningSequenceDirection(board, row, col, 1, 0) or\
               self.winningSequenceDirection(board, row, col,-1, 0)

    # override
    def winningSequenceDirection(self, board, row, col, rowDir, colDir):
        pass