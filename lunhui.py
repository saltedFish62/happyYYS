from utils import *

win  = search()[0]

setPos(win, 0, 0, 600, 0)

images = loadImages()

sleep(0.4, 0.4)

# 是否在选关
def isSelecting():
  # 如果在选关界面
  return len(getEntries()) > 0


# 查找入口列表
def getEntries():
  entries = find(win=win, templ=images['lunhui_entry'])
  return entries


# 战斗
def fighting():
  sleep(1.5, 2)
  while has(win=win, templ=images['vic2']):
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
      clickRange(win=win, box=find(win=win, templ=images['lunhui_start'])[0])
      return


# 全清
def clear():
  while True:
    entries = getEntries()
    if len(entries):
      enter()
      fighting()
    if len(entries) < 1:
      return


clear()
