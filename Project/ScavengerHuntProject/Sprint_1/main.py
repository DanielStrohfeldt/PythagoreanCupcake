from interface import interface
from gameMaker import GameMaker
from game import Game

gmusername = "Admin"
gmpassword = "12345"

g = Game(gmusername, gmpassword)
gm = GameMaker(gmusername, gmpassword, g)
i = interface(g, gm)

while 1:
    response = raw_input("What would you like to do? (type 'help' to get available commands) ")
    if response.strip().lower() == "quit":
        break
    i.command(response)