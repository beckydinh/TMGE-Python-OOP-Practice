from asyncio import create_subprocess_shell
from optparse import BadOptionError
from tkinter.tix import COLUMN
from Game import Game
from Connect4Board import Connect4Board

from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

class Connect4Game(Game):
    def __init__(self):
        super().__init__()
        self.c4 = None
        self.board = []
        self.board_ui = None
        self.red = None
        self.yellow = None

    # def play(self):
    #     if(self.ctrl.getTotalPlayers() < 2):
    #         print("\nNot enough users to play. Please add another user\n")
    #         return
    #     print(str(self.ctrl.currPlayer) + " is RED")
    #     print(str(self.ctrl.player2) + " is YELLOW")
    #     c4 = Connect4Board(6, 7, 2)
    #     while not c4.checkWin():
    #         if c4.getTurn() % 2 == 1:
    #             print("\n" + str(self.ctrl.currPlayer) + "'s turn")
    #             self.red.config(state=ACTIVE)
    #             self.yellow.config(state=DISABLED)
    #         else:
    #             print("\n" + str(self.ctrl.player2) + "'s turn")
    #             self.red.config(state=DISABLED)
    #             self.yellow.config(state=ACTIVE)

    #         c4.printBoard()
    #         while True:
    #             column = int(input("Enter the column to drop: "))
    #             if not c4.isValidColumn(column - 1) or c4.getBottomEmptyRow(column - 1) < 0:
    #                 print("Invalid column, please try again\n")
    #                 continue
    #             if c4.getTurn() % 2 == 1:
    #                 c4.drop("R", column)
    #             else:
    #                 c4.drop("Y", column)
    #             break
    #     c4.printBoard()
    #     if c4.getTurn() % 2 == 0:
    #         print("\n" + str(self.ctrl.currPlayer) + " wins!")
    #         self.ctrl.incrPlayerScore(self.ctrl.currPlayer)
    #     else:
    #         print("\n" + str(self.ctrl.player2) + " wins!")
    #         self.ctrl.incrPlayerScore(self.ctrl.player2)

    def play(self):
        self.c4 = Connect4Board(6, 7, 2)
        
        self.createUI()

    def createUI(self):
        self.board_ui = Tk()
        self.board_ui.geometry("600x500")
        self.board_ui.title("Connect 4")

        self.red = Button(self.board_ui, text=str(self.ctrl.currPlayer) + " is RED", width=11)
        self.yellow = Button(self.board_ui, text=str(self.ctrl.player2) + " is YELLOW", width=11, state=DISABLED)
        self.red.grid(row=1, column=3)
        self.yellow.grid(row=2, column=3)

        self.updateBoard()

    def updateBoard(self):
        rows = len(self.c4.getBoard())
        cols = len(self.c4.getBoard()[0])
        for r in range(rows):
            row = []
            for c in range(cols):
                dropTile = partial(self.userClick, c)
                tile = Button(self.board_ui, command=dropTile, height=4, width=11)
                tile.grid(row=r + 3, column=c)
                row.append(tile)
            self.board.append(row)
        self.board_ui.mainloop()

    def userClick(self, col):
        if self.c4.getTurn() % 2 == 1:
            self.red.config(state=DISABLED)
            self.yellow.config(state=ACTIVE)
        else:
            self.red.config(state=ACTIVE)
            self.yellow.config(state=DISABLED)

        bottomRow = self.c4.getBottomEmptyRow(col)
        if self.c4.isValidColumn(col) and bottomRow >= 0:
            if self.c4.getTurn() % 2 == 1:
                self.c4.drop("R", col)
                self.board[bottomRow][col].config(bg="red")
            else:
                self.c4.drop("Y", col)
                self.board[bottomRow][col].config(bg="yellow")
        self.c4.printBoard()

        if self.c4.checkWin():
            self.board_ui.destroy()
            if self.c4.getTurn() % 2 == 0:
                print("\n" + str(self.ctrl.currPlayer) + " wins!")
                messagebox.showinfo("Winner", str(self.ctrl.currPlayer) + " wins!")
                self.ctrl.incrPlayerScore(self.ctrl.currPlayer)
            else:
                print("\n" + str(self.ctrl.player2) + " wins!")
                messagebox.showinfo("Winner", str(self.ctrl.player2) + " wins!")
                self.ctrl.incrPlayerScore(self.ctrl.player2)

            