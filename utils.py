import win32api
import win32con
import win32gui
import sys
import random
from ctypes import *
import pyautogui
import numpy as np
import cv2


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
    (x1, y1, x2, y2) = box
    x = random.randint(int(x1), int(x2))
    y = random.randint(int(y1), int(y2))
    click(win, x, y)


# 截图窗口
def capture(win):
    active(win)
    rect = win32gui.GetWindowRect(win)
    imageRGB = pyautogui.screenshot(region=(rect[0], rect[1], 600, rect[3]))
    imageGray = cv2.cvtColor(np.asarray(imageRGB), cv2.COLOR_RGB2GRAY)
    return imageGray


if __name__ == "__main__":
    wins = search()
    setPos(wins[0], 0, 0, 600, 0)