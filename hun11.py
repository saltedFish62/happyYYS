from utils import *

players = search()

i = 0
for player in players:
  setPos(player, i * 600, 0, 600, 0)

sleep(1, 1)

