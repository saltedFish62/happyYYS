from utils import *
from res import *

players = search()
playerNum = len(players)

for i, player in enumerate(players):
  setPos(player, i * 600, 0, 600, 0)
  i += 1

sleep(1, 1)

captain = 0
for player in players:
  img=capture(player)
  width, height = img.shape[::-1]
  if has(player, cropImg(img, (0, 0), (width / 4, height))):
    captain = player

if captain == 0:
  print("can't find captain, quit.")
  sys.exit()

members = players[:]
members.remove(captain)
print("players is ", players)
print("captain is ", captain)
print("members is ", members)

def checkPrepare():
  prepared = set()
  while len(prepared) < playerNum:
    for player in players:
      clickRange(player, find(player, prepare))
      if not has(player, prepare):
        prepared.add(player)
  return True

state = "group"
while True:
  if state == "group":
    inviteBtnNum = len(find(captain, invite))
    if inviteBtnNum == 3 - playerNum:
      boxes = find(captain, start)
      if len(boxes) < 1:
        continue
      print(boxes)
      clickRange(captain, boxes[0])
      state = "fighting"
  elif state == "fighting":
    # check prepare
    if checkPrepare():
      state = "end"
  elif state == "end":
    break


