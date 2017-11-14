from user import User
import time


class Team(User):
    def __init__(self, username, password):
        super(Team, self).__init__(username, password)
        self.startTime = None
        self.penalties = 0
        self.iterator = None
        self.totalTime = 0
        self.current_location = None
        self.hasFinished = False
        self.attempted = 0

    def get_starttime(self):
        return self.startTime

    def get_penalites(self):
        return self.penalties

    def start_time(self):
        self.startTime = time.time()

    def end_time(self):
        endTime = time.time()
        self.totalTime = self.totalTime + (endTime - self.startTime)

    def add_penalty(self):
        self.penalties = self.penalties + 1

    def set_iterator(self, iterator):
        self.iterator = iterator

    def get_iterator(self):
        return self.iterator

    def add_attempt(self):
        self.attempted = self.attempted + 1

    def moveon(self):
        if self.iterator:
            try:
                self.attempted = 0
                self.current_location = self.iterator.next()
            except StopIteration:
                self.hasFinished = True
        else:
            print("Cannot move on, team does not have iterator over the current locations")

    def get_finalscore(self):
        if self.hasFinished:
            return self.totalTime + self.penalties
        else:
            return None

    def has_finished(self):
        return self.hasFinished

    def get_attempts(self):
        return self.attempted

    def get_currentlocation(self):
        return self.current_location

    def print_status(self):
        if self.current_location is None:
            curloc = None
        else:
            curloc = self.current_location.get_name()

        if not self.hasFinished:
            print("Team: " + self.username + "  Current location: " + str(curloc) + "  Total time(so far): " +
                  str(self.totalTime) + "  Total penalties: " + str(self.get_penalites()))
        else:
            print("Team: " + self.username + "  Finished game.  Final score = " + str(self.get_finalscore()))
