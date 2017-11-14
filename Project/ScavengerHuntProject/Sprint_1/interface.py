from gameMaker import GameMaker
from playable import Playable
from team import Team


class interface():
    def __init__(self, game, gamemaker):
        if isinstance(game, Playable) and isinstance(gamemaker, GameMaker):
            self.game = game
            self.gamemaker = gamemaker
        else:
            raise TypeError("Invalid types passed into interface class!")

        self.gameMakerCommands = {"logout": lambda: self.game.logout(),
                                  "add location": lambda: self.prompt_addlocation(),
                                  "add team": lambda: self.prompt_addteam(),
                                  "remove team": lambda: self.prompt_removeteam(),
                                  "get status": lambda: self.gamemaker.print_status(),
                                  "end": lambda: self.game.end(), "start": lambda: self.game.start(),
                                  "help": lambda: self.print_commands()}
        self.teamCommands = {"logout": lambda: self.game.logout(),
                             "get status": lambda: self.game.get_currentuser().print_status(),
                             "edit credentials": lambda: self.prompt_editcredentials(), "play": lambda: self.game.play(False),
                             "get clue": lambda: self.print_clue(), "help": lambda: self.print_commands()}
        self.genericCommands = {"login": lambda: self.prompt_login(), "help": lambda: self.print_commands()}

    def command(self, s):
        st = str(s).lower().strip()
        if not isinstance(self.game.get_currentuser(), GameMaker) and not isinstance(self.game.get_currentuser(), Team):
            try:
                self.genericCommands[st]()
            except KeyError:
                print("Invalid command!")
        elif isinstance(self.game.get_currentuser(), GameMaker):
            try:
                self.gameMakerCommands[st]()
            except KeyError:
                print("Invalid command!")
        else:
            try:
                self.teamCommands[st]()
            except KeyError:
                print("Invalid command!")

    def prompt_login(self):
        username = raw_input("Enter your username: ")
        password = raw_input("Enter your password: ")
        self.game.login(username.strip(), password.strip())

    def prompt_addlocation(self):
        name = raw_input("Enter the name of the location: ")
        clue = raw_input("Enter a clue for the location: ")
        question = raw_input("Enter a confirmation question for the location: ")
        answer = raw_input("Enter an answer for the confirmation question: ")
        self.gamemaker.add_location(name.strip(), clue.strip(), question.strip(), answer.strip().lower())

    def prompt_addteam(self):
        name = raw_input("Enter a name for the team to be created: ")
        password = raw_input("Enter a password for the team to be created: ")
        self.gamemaker.add_team(name.strip(), password.strip())

    def prompt_removeteam(self):
        name = raw_input("Enter a name for the team you want to remove: ")
        self.gamemaker.remove_team(name.strip())

    def print_clue(self):
        if self.game.get_currentuser().get_currentlocation is not None:
            print("Clue for next location: " + self.game.get_currentuser().get_currentlocation().get_clue())
        else:
            print("There is not clue for the next location. Either you haven't started playing yet or you have finished"
                  " a game already")

    def prompt_editcredentials(self):
        ins = raw_input("What would you like to change about your team? (enter password or username): ")
        change = ins.strip().lower()
        if change == "password":
            password = raw_input("Enter new password: ")
            self.game.get_currentuser().set_password(password.strip())
        elif change == "username":
            username = raw_input("Enter new username: ")
            if self.game.get_teamset().get(username) is None:
                self.game.get_currentuser().set_username(username.strip())
            else:
                print("Cannot change username, a team with this username already exists")

    def print_commands(self):
        print("***** Commands *****")
        if self.game.get_currentuser() is None:
            for key in self.genericCommands.keys():
                print(key)
        elif isinstance(self.game.get_currentuser(), GameMaker):
            for key in self.gameMakerCommands.keys():
                print(key)
        else:
            for key in self.teamCommands.keys():
                print(key)
        print("********************")


