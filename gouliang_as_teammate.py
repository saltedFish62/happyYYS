from utils import *

images = loadImages()

# 在探索场景?
def isInTansuo(img):
  return has(image=img, templ=images[''])


# 队长退了？
def isCaptainExit(img):
  return has(image=img, templ=images[''])
