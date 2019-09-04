<<<<<<< HEAD
from transitions import Machine
import time

states = [
    "group",
    "fight_pre",
    "fighting",
    "fighting_p3",
    "vic",
    "fail",
    "reinvite",
    "invite_default",
    "accept_default"
]

transitions = [
    {'trigger': 'start', 'source': 'group', 'dest': 'fight_pre',
        'prepare': '_start', 'conditions': 'hasStarted'},
    {'trigger': 'prepare', 'source': 'fight_pre', 'dest': 'fighting',
     'prepare': '_prepare', 'conditions': 'hasPrepared'},
    {'trigger': 'fight', 'source': 'fighting', 'dest': 'fighting_p3',
     'prepare': '_fight', 'conditions': 'isFightingP3'},
    {'trigger': 'checkEnd', 'source': 'fighting_p3', 'dest': 'vic',
     'prepare': 'fight_p3', 'conditions': 'isVic'},
    {'trigger': 'checkEnd', 'source': 'fighting_p3', 'dest': 'fail',
     'prepare': 'fight_p3', 'conditions': 'isFail'},
    {'trigger': 'checkVic', 'source': 'vic', 'dest': 'invite_default',
     'prepare': '_checkVic', 'conditions': 'needInviteDefault'},
    {'trigger': 'checkVic', 'source': 'vic', 'dest': 'group',
     'prepare': '_checkVic', 'conditions': 'isInGroup'},
    {'trigger': 'defaultInvite', 'source': 'invite_default', 'dest': 'group',
     'prepare': 'setInviteDefault', 'conditions': 'isInGroup'},
    {'trigger': 'checkFail', 'source': 'fail', 'dest': 'reinvite',
     'prepare': '_checkFail', 'conditions': 'needReinvite'},
    {'trigger': 'reinvite', 'source': 'reinvite', 'dest': 'group',
     'prepare': '_reinvite', 'conditions': 'isInGroup'}
]


class Hun11(object):
    needDe = True
    _times = 0

    def __init__(self, captain, players):
        self.captain = captain
        self.members = players[:]
        self.members.remove(captain)

    # 如果队伍人数满足要求则开车 否则不停更新 直到人齐点击开始战斗
    def _start(self):
        print('start')

    # 如果已经开始则返回 True
    def hasStarted(self):
        return True

    # 进入战斗 点击各个队员的准备
    def _prepare(self):
        print('prepare')

    # 是否全员准备 查询队长是否存在准备按钮 否则返回true
    def hasPrepared(self):
        return True

    # 前两回合的战斗 间隔为 2s 点击中间的怪
    def _fight(self):
        print('fight')

    # 判断是否到了p3打大蛇的阶段 是则返回True
    def isFightingP3(self):
        return True

    # 打大蛇时疯狂点击大蛇
    def fight_p3(self):
        print('p3')

    # 是否胜利
    def isVic(self):
        return self._times % 2 == 1
=======
from utils import *
from res import *

players = search()
playerNum = len(players)

for i, player in enumerate(players):
  setPos(player, i * 600, 0, 600, 0)
  i += 1
>>>>>>> 47a0c398446989a93dae153ea1b185464ff38fdd

    # 是否失败
    def isFail(self):
        return self._times % 2 == 0

<<<<<<< HEAD
    # 胜利：点击结算奖励 需要判断两种 一种是胜利的鼓 一种是红蛋 两种都是胜利条件
    def _checkVic(self):
        print('checkVic')

    # 是否需要设置默认邀请队友
    def needInviteDefault(self):
        return self.needDe

    # 是否在组队界面
    def isInGroup(self):
        return True

    # 设置默认邀请 队长发出默认邀请 队员接受默认邀请
    def setInviteDefault(self):
        print('default')

    # 失败：点击失败 判断条件为失败的败字
    def _checkFail(self):
        print('fail')

    # 失败后队长会有是否重新邀请的框 判断是否进入重新邀请的流程
    def needReinvite(self):
        return True

    # 重新邀请的操作 队长点击确认 队员同意邀请
    def _reinvite(self):
        print('reinvite')


captain = 1
players = [1, 2, 3]

hun11 = Hun11(captain, players)
machine = Machine(model=hun11, states=states,
                  transitions=transitions, initial="group")

i = 0
try:
    while i < 10:
        while not hun11.start():
            print("组队中，队员未齐")
        while not hun11.prepare():
            print("战斗准备")
        while not hun11.fight():
            print("前两回合战斗")
        while not hun11.checkEnd():
            print("打大蛇")
        if hun11.state == 'fail':
            while not hun11.checkFail():
                print("失败")
            while not hun11.reinvite():
                print("重新邀请")
        else:
            while not hun11.checkVic():
                print("胜利！")
        if hun11.state == 'invite_default':
            while not hun11.defaultInvite():
                print("设置默认邀请")
except KeyboardInterrupt:
    print('quit')
=======
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


>>>>>>> 47a0c398446989a93dae153ea1b185464ff38fdd
