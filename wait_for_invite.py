from utils import *

win  = search()[0]

setPos(win, 0, 0, 600, 0)

images = loadImages()

while 1:
  locs = find(win=win, templ=images['accept_invite'])
  if len(locs) > 0:
    clickRange(win=win, box=locs[0])
  if has(image=img, templ=images['vic1']) or has(image=img, templ=images['vic2']):
    clickRange(win=win, box=(500, 60, 20, 10))
  sleep(1, 2)
