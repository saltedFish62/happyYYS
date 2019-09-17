from transitions import Machine
from utils import *
import sys

states = [
    'creating_group',
    'invite',
    'scene',
    'prepare',
    'change_mon',
    'fighting',
    'moving_scene',
    'exit',
    'check_invite',
    'reinvite',
    'set_up'
]

transitions = [
    {'trigger': 'findTeammate', 'source': 'creating_group',
        'dest': 'invite', 'conditions': 'hasTeammate'},
    {'trigger': 'enter', 'source': 'invite', 'dest': 'scene',
     'prepare': 'inviteTeammate', 'conditions': 'isInScene'},
    {'trigger': 'findExp', 'source': 'scene', 'dest': 'prepare',
     'prepare': 'clickExp', 'conditions': 'isPreparing'},
    {'trigger': 'checkMon', 'source': 'prepare',
     'dest': 'change_mon', 'conditions': 'needChangeMon'},
    {'trigger': 'checkMon', 'source': 'prepare',
     'dest': 'fighting', 'conditions': 'canFight'},
    {'trigger': 'changeMon', 'source': 'change_mon', 'dest': 'fighting',
     'prepare': 'changeMonster', 'conditions': 'canFight'},
    {'trigger': 'checkAward', 'source': 'fighting', 'dest': 'scene',
     'prepare': 'clickAward', 'conditions': 'isInScene'},
    {'trigger': 'noExp', 'source': 'scene',
     'dest': 'moving_scene', 'conditions': 'hasNotMoved'},
    {'trigger': 'noExp', 'source': 'scene',
        'dest': 'exit', 'conditions': 'hasMoved'},
    {'trigger': 'moveScene', 'source': 'moving_scene', 'dest': 'scene',
     'prepare': 'moveSceneToRight', 'conditions': 'isTheEndOfScene'},
    {'trigger': 'goOut', 'source': 'exit', 'dest': 'check_invite',
     'prepare': 'goOutOfScene', 'conditions': 'isOut'},
    {'trigger': 'checkInvite', 'source': 'check_invite',
     'dest': 'reinvite', 'conditions': 'hasReinvite'},
    {'trigger': 'checkInvite', 'source': 'check_invite',
     'dest': 'set_up', 'conditions': 'canNotReinvite'},
    {'trigger': 'reinvite', 'source': 'reinvite', 'dest': 'scene',
     'prepare': 'checkReinvite', 'conditions': 'isInScene'},
    {'trigger': 'setUp', 'source': 'set_up', 'dest': 'creating_group',
     'prepare': 'setUpGroup', 'conditions': 'isCreating'},
]

# images = loadImages()


class Gouliang(object):
    def __init__(self, captain, teammate):
        self.captain = captain
        self.teammate = teammate
        self.hasMoved = False
        self.teammateImg = 0

    # 是否有队友

    def hasTeammate(self):
        # 把队友头像截下来
        img = capture(self.captain)
        loc = find(image=img, templ=images['teammate'])
        if len(loc) > 0:
            tl = loc[0]
            if self.teammateImg == 0:
                tmImg = cropImg(img=img, topLeft=(
                    tl[0] - 110, tl[1]), bottomRight=(tl[0]-70, tl[1]+40))
                self.teammateImg = tmImg
            return True
        else:
            if self.teammateImg != 0:
                tm = find(image=img, templ=self.teammateImg)
                if len(tm) > 0:
                    clickRange(win=self.captain, box=tm[0])
        sleep(0.5, 0.5)
        return False

    # 邀请队友

    def inviteTeammate(self):
        locs = find(win=self.captain, templ=images['captain1'])
        print(locs)
        if len(locs) > 0:
            clickRange(win=self.captain, box=locs[0])
            sleep(0.5, 0.6)
            while True:
                locs = find(win=self.teammate, templ=images['accept_invite'])
                if len(locs) > 0:
                    clickRange(win=self.teammate, box=locs[0])
                sleep(0.3, 0.3)
                break

    # 是否队员和队友都在场景里

    def isInScene(self):
        return has(win=self.captain, templ=images['is_in_scene'])

    # 找经验怪并点击

    def clickExp(self):
        pass

    # 进入准备界面

    def isPreparing(self):
        pass

    # 是否需要换狗粮

    def needChangeMon(self):
        pass

    # 符合开始战斗条件

    def canFight(self):
        pass

    # 换狗粮

    def changeMonster(self):
        pass

    # 点击奖励

    def clickAward(self):
        pass

    # 划屏到右边

    def moveSceneToRight(self):
        pass

    # 已经在最右边了

    def isTheEndOfScene(self):
        pass

    # 已经划屏了

    def hasMoved(self):
        return self.hasMoved

    # 还没有划屏

    def hasNotMoved(self):
        return not self.hasMoved

    # 退出场景

    def goOutOfScene(self):
        pass

    # 是否已经退出场景

    def isOut(self):
        pass

    # 可以重新邀请

    def hasReinvite(self):
        pass

    # 不能重新邀请

    def canNotReinvite(self):
        pass

    # 队长发出重新邀请 队员同意

    def checkReinvite(self):
        pass

    # 进入组队邀请界面

    def setUpGroup(self):
        pass

    # 在组队选择界面

    def isCreating(self):
        pass


images = loadImages()

captain = 0
teammate = 0

players = search()

i = 0
for player in players:
    setPos(player, i*600, 0, 600, 0)
    i += 1

sleep(0.6, 0.6)
if has(win=players[0], templ=images['captain1']):
    captain = players[0]
    teammate = players[1]
else:
    captain = players[1]
    teammate = players[0]

if captain == 0:
    print('找不到队长')
    sys.exit()

print('队长是', captain)

gouliang = Gouliang(captain, teammate)
machine = Machine(model=gouliang, states=states,
                  transitions=transitions, initial='creating_group')

times = 0
try:
    while True:
        while not gouliang.findTeammate():
            pass
        while not gouliang.enter():
            print('进入战斗')
        start = now()
        while now() - start < 2:
            
except KeyboardInterrupt:
    print('quit')
