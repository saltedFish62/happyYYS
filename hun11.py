from transitions import Machine
from utils import *
import sys

states = [
    "group",
    "fight_pre",
    "fighting",
    "fighting_p3",
    "end_fight",
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
     'conditions': 'hasPrepared'},
    {'trigger': 'fight', 'source': 'fighting', 'dest': 'fighting_p3',
     'prepare': '_fight', 'conditions': 'isFightingP3'},
    {'trigger': 'checkFight', "source": "fighting_p3",
     'prepare': 'fight_p3', 'dest': 'end_fight', 'conditions': 'isEnd'},
    {'trigger': 'checkEnd', 'source': 'end_fight',
     'dest': 'vic', 'conditions': 'isVic'},
    {'trigger': 'checkEnd', 'source': 'end_fight',
     'dest': 'fail', 'conditions': 'isFail'},
    {'trigger': 'checkVic', 'source': 'vic', 'dest': 'invite_default',
     'prepare': 'check', 'conditions': 'needInviteDefault'},
    {'trigger': 'checkVic', 'source': 'vic', 'dest': 'group',
     'prepare': 'check', 'conditions': 'isFightEnd'},
    {'trigger': 'defaultInvite', 'source': 'invite_default', 'dest': 'group',
     'prepare': 'setInviteDefault', 'conditions': 'isFightEnd'},
    {'trigger': 'checkFail', 'source': 'fail', 'dest': 'reinvite',
     'prepare': 'check', 'conditions': 'needReinvite'},
    {'trigger': 'reinvite', 'source': 'reinvite', 'dest': 'group',
     'prepare': '_reinvite', 'conditions': 'isFightEnd'}
]

images = loadImages()

class Hun11(object):
    def __init__(self, captain, players):
        self.captain = captain
        self.members = players[:]
        self.members.remove(captain)
        self.players = players

    # 如果队伍人数满足要求则开车 否则不停更新 直到人齐点击开始战斗
    def _start(self):
        image = capture(self.captain)
        locs = find(templ=images['invite'], image=image)
        if len(locs) == 2 - len(self.members):
            locs = find(templ=images['start'], win=self.captain)
            if len(locs) == 1:
                clickRange(self.captain, locs[0])
        sleep(0.2, 0.4)

    # 如果已经开始则返回 True
    def hasStarted(self):
        sleep(2.4, 2.5)
        img = capture(self.captain)
        if has(image=img, templ=images['prepare']):
            return True
        if has(image=img, templ=images['fight']):
            return True
        return False

    # 是否全员准备 查询队长是否存在准备按钮 否则返回true
    def hasPrepared(self):
        sleep(0.5, 0.5)
        return not has(win=self.captain, templ=images['prepare'])

    # 前两回合的战斗 间隔为 2s 点击中间的怪
    def _fight(self):
        clickRange(self.captain, (270, 80, 40, 30))
        sleep(1, 2)
        if getPos()[0] < 10:
            sys.exit()

    # 判断是否到了p3打大蛇的阶段 是则返回True
    def isFightingP3(self):
        return has(win=self.captain, templ=images['hun11_p3'])

    # 打大蛇时疯狂点击大蛇
    def fight_p3(self):
        clickRange(self.captain, (270, 80, 60, 30))

    # 判断战斗是否结束
    def isEnd(self):
        return not has(win=self.captain, templ=images["hun11_p3"])

    # 是否胜利
    def isVic(self):
        if has(win=self.captain, templ=images['vic1']):
            return True
        if has(win=self.captain, templ=images['vic2']):
            return True
        return False

    # 是否失败
    def isFail(self):
        if has(win=self.captain, templ=images['fail']):
            return True
        return False

    # 胜利：点击结算奖励 需要判断两种 一种是胜利的鼓 一种是红蛋 两种都是胜利条件
    def check(self):
        for player in players:
            img = capture(player)
            if has(image=img, templ=images['vic1']) or has(image=img, templ=images['vic2']):
                clickRange(win=player, box=(500, 60, 20, 10))
        sleep(1, 1.6)

    # 是否需要设置默认邀请队友
    def needInviteDefault(self):
        return has(win=self.captain, templ=images['default_invite'])

    # 是否在组队界面
    def isFightEnd(self):
        for player in self.players:
            if has(win=player, templ=images['is_fighting']):
                return False
        return True

    # 设置默认邀请 队长发出默认邀请 队员接受默认邀请
    def setInviteDefault(self):
        while has(win=self.captain, templ=images['default_invite']):
            locs = find(image=capture(self.captain),
                        templ=images['is_invite_default_uncheck'])
            if len(locs):
                clickRange(self.captain, (locs[0][0], locs[0][1], 17, 17))
                sleep(0.1, 0.3)
                clickRange(
                    self.captain, (locs[0][0]+60, locs[0][1]+30, 60, 20))
                sleep(0.5, 0.5)
        sleep(1.4, 1.6)
        for player in self.members:
            while 1:
                sleep(0.2, 0.3)
                locs = find(win=player, templ=images['accept_default_invite'])
                if len(locs) != 0:
                    clickRange(player, locs[0])
                    break

    # 失败后队长会有是否重新邀请的框 判断是否进入重新邀请的流程
    def needReinvite(self):
        return has(win=self.captain, templ=images['reinvite'])

    # 重新邀请的操作 队长点击确认 队员同意邀请
    def _reinvite(self):
        locs = find(win=self.captain, templ=images['reinvite'])
        if len(locs) > 0:
            clickRange(win=self.captain, box=(
                locs[0][0]+130, locs[0][1]+80, 60, 25))
            sleep(1, 1.5)
            for player in self.members:
                clickRange(player, find(
                    win=player, templ=images['accept_invite'])[0])


captain = 0
players = search()

i = 0
for player in players:
    setPos(player, i*600, 0, 600, 0)
    i += 1

sleep(0.6, 0.6)

for player in players:
    img = capture(player)
    _, height = img.shape[::-1]
    if has(image=cropImg(img, (0, 0), (150, height)), templ=images['captain']):
        captain = player

if captain == 0:
    print('找不到队长')
    quitScript()

hun11 = Hun11(captain, players)
machine = Machine(model=hun11, states=states,
                  transitions=transitions, initial="group")

times = 0
try:
    while 1:
        while not hun11.start(): pass
        while not hun11.prepare(): pass
        while not hun11.fight(): pass
        while not hun11.checkFight(): pass
        while not hun11.checkEnd(): pass
        if hun11.state == 'fail':
            while not hun11.checkFail():
                print("失败")
            while not hun11.reinvite():
                print("重新邀请")
        else:
            while not hun11.checkVic(): pass
        if hun11.state == 'invite_default':
            while not hun11.defaultInvite(): pass
        times += 1
        print(times, '次')
except KeyboardInterrupt:
    print('quit')
