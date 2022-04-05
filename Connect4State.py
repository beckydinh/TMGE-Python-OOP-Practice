from Board import Board
from State import State

class Connect4State(State):
    def __init__(self, totalPlayers):
        super().__init__(totalPlayers)

    def isWinningSequence(self, board, row, col):
        return self.winningSequenceDirection(board, row, col, 0, 1) or\
               self.winningSequenceDirection(board, row, col, 1, 1) or\
               self.winningSequenceDirection(board, row, col, 1, 0) or\
               self.winningSequenceDirection(board, row, col, 1,-1) or\
               self.winningSequenceDirection(board, row, col, 0,-1) or\
               self.winningSequenceDirection(board, row, col,-1,-1) or\
               self.winningSequenceDirection(board, row, col,-1, 0) or\
               self.winningSequenceDirection(board, row, col,-1, 1)

    def winningSequenceDirection(self, board: Board, row, col, rowDir, colDir):
        boardArray = board.boardArray
        currTile = boardArray[row][col]
        if currTile == None:
            return False
        else:
            for i in range(1, 4):
                if not board.isValidRow(row + rowDir * i) or\
                   not board.isValidColumn(col + colDir * i) or\
                   boardArray[row + rowDir * i][col + colDir * i] == None or\
                   boardArray[row + rowDir * i][col + colDir * i].value != currTile.value:
                   return False 
            return True
