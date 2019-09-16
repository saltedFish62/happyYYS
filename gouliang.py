from transitions import Machine

states: [
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
  {'trigger': 'findTeammate', 'source': 'creating_group', 'dest': 'invite', 'conditions': 'hasTeammate'},
  {'trigger': 'enter', 'source': 'invite', 'dest': 'scene', 'prepare': 'inviteTeammate', 'conditions': 'isInScene'},
  {'trigger': 'findExp', 'source': 'scene', 'dest': 'prepare', 'prepare': 'clickExp', 'conditions': 'isPreparing'},
  {'trigger': 'checkMon', 'source': 'prepare', 'dest': 'change_mon', 'conditions': 'needChangeMon'},
  {'trigger': 'checkMon', 'source': 'prepare', 'dest': 'fighting', 'conditions': 'canFight'},
  {'trigger': 'changeMon', 'source': 'change_mon', 'dest': 'fighting', 'prepare': 'changeMonster', 'conditions': 'canFight'},
  {'trigger': 'checkAward', 'source': 'fighting', 'dest': 'scene', 'prepare': 'clickAward', 'conditions': 'isInScene'},
  {'trigger': 'noExp', 'source': 'scene', 'dest': 'moving_scene', 'conditions': 'hasNotMoved'},
  {'trigger': 'noExp', 'source': 'scene', 'dest': 'exit', 'conditions': 'hasMoved'},
  {'trigger': 'moveScene', 'source': 'moving_scene', 'dest': 'scene', 'prepare': 'moveSceneToRight', 'conditions': 'isTheEndOfScene'},
  {'trigger': 'goOut', 'source': 'exit', 'dest': 'check_invite', 'prepare': 'goOutOfScene', 'conditions': 'isOut'},
  {'trigger': 'checkInvite', 'source': 'check_invite', 'dest': 'reinvite', 'conditions': 'hasReinvite'},
  {'trigger': 'checkInvite', 'source': 'check_invite', 'dest': 'set_up', 'conditions': 'canNotReinvite'},
  {'trigger': 'reinvite', 'source': 'reinvite', 'dest': 'scene', 'prepare': 'checkReinvite', 'conditions': 'isInScene'},
  {'trigger': 'setUp', 'source': 'set_up', 'dest': 'creating_group', 'prepare': 'setUpGroup', 'conditions': 'isCreating'},
]

# images = loadImages()

class Gouliang(object):
    def __init__(self, captain, teammate):
        self.captain = captain
        self.teammate = teammate
        self.hasMoved = False

    
    # 是否有队友
    def hasTeammate(self):
      # 把队友头像截下来
      pass


    # 邀请队友
    def inviteTeammate(self):
      pass


    # 是否队员和队友都在场景里
    def isInScene(self):
      pass


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


captain = 0
teammate = 1

# find captain and teammate

gouliang = Gouliang(captain, teammate)
machine = Machine(model=gouliang, states=states,
                  transitions=transitions, initial='grouping')

times = 0
try:
    while True:
      pass
except KeyboardInterrupt:
    print('quit')
