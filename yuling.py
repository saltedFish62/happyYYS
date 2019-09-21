from utils import *

win = 0
win = search()[0]

if win == 0:
  print('no onmychi')
  quitScript()

setPos(win, 0, 0, 600, 0)

images = loadImages()

while True:
  img = capture(win)
  locs = find(image=img, templ=images['yuling_entry'])
  if len(locs) > 0:
    clickRange(win, locs[0])
  locs1 = find(image=img, templ=images['vic1'])
  if len(locs1) > 0:
    clickRange(win, locs1[0])
  locs2 = find(image=img, templ=images['vic2'])
  if len(locs2) > 0:
    clickRange(win, locs2[0])
  sleep(1, 2)
