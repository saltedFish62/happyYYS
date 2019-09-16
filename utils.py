import win32api
import win32con
import win32gui
import sys
import random
from ctypes import *
import pyautogui
import numpy as np
import time
import cv2
import os

import matplotlib.pyplot as plt


# search for the windows of yys
def search():
    hList = []
    rList = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hList)
    for h in hList:
        title = win32gui.GetWindowText(h)
        clsname = win32gui.GetClassName(h)
        if clsname == 'Win32Window0' and title == '阴阳师-网易游戏':
            rList.append(h)
    return rList


# 激活窗口
def active(win):
    windll.user32.SwitchToThisWindow(win, True)


# 设置窗口位置和大小
def setPos(win, x, y, w, h):
    win32gui.SetWindowPos(win, win32con.HWND_TOP, x,
                          y, w, h, win32con.SWP_SHOWWINDOW)
    # win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, x,
    #                      y, w, h, win32con.SWP_SHOWWINDOW)


def getPos(win):
    return win32gui.GetWindowRect(win)


# 点击窗口的坐标
def click(win, delX, delY):
    left, top, _, _ = win32gui.GetWindowRect(win)
    pyautogui.click(left + delX, top + delY)


# 点击窗口的范围
def clickRange(win, box):
    (left, top, w, h) = box
    x = random.randint(int(left), int(left+w))
    y = random.randint(int(top), int(top+h))
    click(win, x, y)

# 截图窗口
def capture(win):
    active(win)
    rect = win32gui.GetWindowRect(win)
    imageRGB = pyautogui.screenshot(region=(rect[0], rect[1], 600, rect[3]))
    return cv2.cvtColor(np.asarray(imageRGB), cv2.COLOR_RGB2GRAY)


# 模板匹配查找
def find(templ, image=[], win=0):
    if win != 0:
        img = capture(win)
    else:
        img = image
    
    templW, templH = templ.shape[::-1]
    matchResult = cv2.matchTemplate(img, templ, cv2.TM_CCOEFF_NORMED)

    locs = np.where(matchResult >= 0.85)
    result = []
    for pt in zip(*locs[::-1]):
        result.append((pt[0], pt[1], templW, templH))
        # (x, y, width, height)
    return result


# 是否存在
def has(templ, image=[], win=0):
    return len(find(win=win, image=image, templ=templ)) != 0

# 休眠一段时间
def sleep(min, max):
    if min == max:
        time.sleep(min)
    else:
        time.sleep(random.randint(int(min*10), int(max*10)) / 10)


# 切割图片
def cropImg(img, topLeft, bottomRight):
    w, h = img.shape[::-1]
    left = topLeft[0] if topLeft[0] >= 0 else 0
    top = topLeft[1] if topLeft[1] >= 0 else 0
    right = bottomRight[0] if bottomRight[0] < w else w-1
    bottom = bottomRight[1] if bottomRight[1] < h else h-1
    return img[int(top) : int(bottom), int(left) : int(right)]

# 灰度读取图片
def readImg(path):
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# 加载图片
def loadImages():
    images = {}
    path = os.getcwd() + '/images'
    imgList = os.listdir(path)

    for img in imgList:
        name = img.split('.')[0]
        images[name] = readImg(path+'/'+img)
    return images

# 获取鼠标位置
def getPos():
    return pyautogui.position()

# 获取当前时间节点
def now():
    return time.process_time()

if __name__ == "__main__":
    # img = readImg('./screen/yaoqing.png')
    img = readImg('./screen/win.png')
    templ = readImg('./images/is_fighting.png')
    print(find(image=img, templ=templ))
    pass