import win32api
import win32con
import win32gui
import sys
import random
from ctypes import *
import pyautogui
import numpy as np


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
    return pyautogui.screenshot(region=(rect[0], rect[1], 600, rect[3]))


# 模板匹配查找
def find(img, path):
    templLoc = pyautogui.locateAll(img, path, grayscale=True, confidence=0.8)
    return list(templLoc)

if __name__ == "__main__":
    pass