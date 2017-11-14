from user import User
from playable import Playable
from team import Team
from loc import Loc

class GameMaker(User):
    def __init__(self, username, password, game):
        super(GameMaker, self).__init__(username, password)
        if isinstance(game, Playable):
            self.game = game

    def add_location(self, name, clue, question, answer):
        if self.game.is_running():
            print("You cannot add a location while the game is being played")
        else:
            l = Loc(name, question, answer, clue)
            locationset = self.game.get_locationset()
            val = locationset.add(l)
            if val:
                print("Location '" + name + "' has been successfully added to the game")
            else:
                print("Location '" + name + "' could not be added to the game, this location already exists")

    def add_team(self, username, password):
        t = Team(username, password)
        teamset = self.game.get_teamset()
        val = teamset.add(t)
        if val:
            print("Team '" + username + "' has been successfully added to the game")
        else:
            print("Team '" + username + "' could not be added to the game, this team already exists")

    def remove_team(self, name):
        teamset = self.game.get_teamset()
        t = Team(name, "")
        val = teamset.remove(t)
        if val:
            print("Team '" + name + "' was successfully removed")
        else:
            print("Team '" + name + "'could not be removed, the team does not exist")

    def print_status(self):
        it = self.game.get_teamset().iterator()
        while(1):
            try:
                t = it.next()
                t.print_status()
            except StopIteration:
                break
