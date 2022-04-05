from Controller import Controller

class Game:
    def __init__(self):
        self.ctrl = Controller()

    def start(self):
        shouldExit = True
        while shouldExit:
            print("1.) Add new user")
            print("2.) Login")
            print("3.) View user scores")
            print("4.) Quit")
            cmd = input("Enter Command Number: ")

            if cmd == "1":
                self.addNewUser()
            elif cmd == "2":
                self.presentLogInDialog()
            elif cmd == "3":
                self.viewCurrUserScore()
            elif cmd == "4":
                shouldExit = False
            else:
                print("\nNot an option!\n")

    def viewCurrUserScore(self):
        print("\n" + str(self.ctrl.currPlayer) + "'s total score: " + str(self.ctrl.getUserScore(self.ctrl.currPlayer)) + "\n")

    def addNewUser(self):
        while True:
            name = input("\nEnter new username: ")
            if self.ctrl.playerNameExists(name):
                print(name + " already exists")
                continue
            self.ctrl.createProfile(name)
            break
        print()

    def presentLogInDialog(self):
        if self.ctrl.getTotalPlayers() < 2:
            print("\nNot enough users to play. Please add another user\n")
            return
        while True:
            print("\nLogin as a user from the list below")
            self.ctrl.printPlayers()
            name1 = input("Login Player1 as: ")
            name2 = input("Login Player2 as: ")

            if self.logInUsers(name1, name2):
                break
        self.play()

    def logInUsers(self, username, user2):
        if not self.ctrl.playerNameExists(username):
            print(str(username) + " does not exist")
            return False
        if not self.ctrl.playerNameExists(user2):
            print(str(user2) + " does not exist")
            return False
        self.ctrl.loginCurrPlayer(username)
        self.ctrl.loginPlayer2(user2)
        print("\nLogged in player 1 as " + str(username) + "\n")
        print("\nLogged in player 2 as " + str(user2) + "\n")
        return True

    # override
    def play():
        pass
        
        