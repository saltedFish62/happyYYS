from utils import *

win  = search()[0]

setPos(win, 0, 0, 600, 0)

images = loadImages()


# 是否在选关
def isSelecting():
  # 如果在选关界面
  len(getEntries()) > 0


# 查找入口列表
def getEntries():
  return find(win=win, templ=images['lunhui_entry'])


# 战斗
def fighting():
  sleep(1.5, 2)
  while not isSelecting():
    clickRange(win=win, box=(500, 60, 20, 10))
    sleep(1.5, 2)


# 选择入口
def enter():
  entries = getEntries()
  for enter in entries:
    clickRange(win=win, box=enter)
    sleep(0.2, 0.2)
    if not isSelecting():
      sleep(0.3, 0.3)
      clickRange(win=win, box=find(win=win, templ=images['lunhui_start']))
      return


# 全清
def clear():
  while True:
    if isSelecting():
      enter()
      fighting()
    if len(getEntries()) < 1:
      return


clear()
