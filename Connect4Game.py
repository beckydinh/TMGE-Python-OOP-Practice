from Game import Game
from Connect4Board import Connect4Board

class Connect4Game(Game):
    def __init__(self):
        super().__init__()

    def play(self):
        if(self.ctrl.getTotalPlayers() < 2):
            print("\nNot enough users to play. Please add another user\n")
            return
        print(str(self.ctrl.currPlayer) + " is RED")
        print(str(self.ctrl.player2) + " is YELLOW")
        c4 = Connect4Board(6, 7, 2)
        while not c4.checkWin():
            if c4.getTurn() % 2 == 1:
                print("\n" + str(self.ctrl.currPlayer) + "'s turn")
            else:
                print("\n" + str(self.ctrl.player2) + "'s turn")
            c4.printBoard()
            while True:
                column = int(input("Enter the column to drop: "))
                if not c4.isValidColumn(column - 1) or c4.getBottomEmptyRow(column - 1) < 0:
                    print("Invalid column, please try again\n")
                    continue
                if c4.getTurn() % 2 == 1:
                    c4.drop("R", column)
                else:
                    c4.drop("Y", column)
                break
        c4.printBoard()
        if c4.getTurn() % 2 == 0:
            print("\n" + str(self.ctrl.currPlayer) + " wins!")
            self.ctrl.incrPlayerScore(self.ctrl.currPlayer)
        else:
            print("\n" + str(self.ctrl.player2) + " wins!")
            self.ctrl.incrPlayerScore(self.ctrl.player2)