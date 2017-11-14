from playable import Playable
from gameMaker import GameMaker
from teamSet import TeamSet
from locationSet import LocationSet


class Game(Playable):
    def __init__(self, gmusername, gmpassword):
        self.gmusername = gmusername
        self.gmpassword = gmpassword
        self.teams = TeamSet()
        self.locations = LocationSet()
        self.currentUser = None
        self.running = False

    def login(self, username, password):
        t = self.teams.get(username)
        if t is None and username != self.gmusername:
            print("Cannot login, this user does not exist!")
        elif (t is not None and t.get_password() != password) or (username == self.gmusername and self.gmpassword != password):
            print("Cannot login, password is incorrect!")
        elif username == self.gmusername:
            self.currentUser = GameMaker(self.gmusername, self.gmpassword, None)
            print(username + ", you are successfully logged in!")
        else:
            self.currentUser = t
            if t.get_iterator() is None:
                t.set_iterator(self.locations.iterator())
            print(username + ", you are successfully logged in!")

    def logout(self):
        if self.currentUser is not None:
            print(self.currentUser.get_username() + ", you have been successfully logged out!")
            self.currentUser = None

    def play(self, hasArrived):
        arrived = ""
        if self.locations.size() == 0:
            print("Cannot play the scavenger hunt game, there are no locations!")
            return
        if not self.running:
            print("You cannot play yet, the game is not currently in session")
            return
        if self.currentUser.has_finished():
            print("You have already finished a game")
            return
        if self.currentUser.get_currentlocation() is None:
            self.currentUser.moveon()
        if not hasArrived:
            print("Here is the clue to your upcoming location: " + self.currentUser.get_currentlocation().get_clue())
            arrived = raw_input("Type 'here' when you arrive at the location: ")
            arrived = arrived.strip().lower()
        if arrived == "here" or hasArrived is True:
            self.currentUser.start_time()
            print("The confirmation question for you location is: " + self.currentUser.get_currentlocation().get_question())
            response = raw_input("What is your answer to this question? ")
            self.answer(response)

    # helper method for the play method
    def answer(self, response):
        if response == self.currentUser.get_currentlocation().get_answer():
            print("Your answer to the question was correct!")
            self.currentUser.moveon()
        else:
            print("Your answer to the question was incorrect. 1 penalty added and 1 attempt added")
            self.currentUser.add_attempt()
            self.currentUser.add_penalty()
            if self.currentUser.get_attempts() == 3:
                print("You have reached the maximum number of attempts to answer this question, now you must move on.")
                self.currentUser.moveon()
            else:
                print("You have " + str(3 - self.currentUser.get_attempts()) + " attempts left to answer the question")
                self.play(True)
        self.currentUser.end_time()

    def get_teamset(self):
        return self.teams

    def get_locationset(self):
        return self.locations

    def get_currentuser(self):
        return self.currentUser

    def start(self):
        if self.teams.size() != 0 and self.locations.size() != 0:
            print("The game has been started!")
            self.running = True
        else:
            print("You cannot start a game without teams or locations")

    def end(self):
        self.running = False
        print("The game has ended!")
        it = self.teams.iterator()
        bestteam = None
        try:
            bestteam = it.next()
        except StopIteration:
            pass
        for x in range(self.teams.size() - 1):
            try:
                team = it.next()
                if team.get_finalscore() is not None and team.get_finalscore() < bestteam.get_finalscore():
                    bestteam = team
            except StopIteration:
                break
        if bestteam is not None and bestteam.get_finalscore() is None:
            print("No winner since no team has played the game!")
        elif bestteam is not None and bestteam.get_finalscore is not None:
            print("Winner of the scavenger hunt game is team " + bestteam.get_username() + " with a score of " +
                    str(bestteam.get_finalscore()))
        else:
            print("No winner since there are no teams!")

    def is_running(self):
        return self.running
