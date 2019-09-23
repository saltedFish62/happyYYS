from transitions import Machine
from utils import *


class Gouliang(object):
    def __init__(self, captain, teammate):
        self.captain = captain
        self.teammate = teammate

    def hasEntered(self):
        img = capture(self.captain)
        # 如果已经在场景里
        if has(image=img, templ=images['is_in_scene']):
            return True
        
        entry = find(image=img, templ=images['gouliang_entry'])
        if len(entry) > 0:
            print('has entry')
            clickRange(win=self.captain, box=entry[0])
        
        if has(image=img, templ=images['gouliang_is_grouping_1']):
            print('entered')
            group = find(image=img, templ=images['group'])
            if len(group) > 0:
                print('group')
                clickRange(win=self.captain, box=group[0])
            else:
                hard = find(image=img, templ=images['gouliang_hard'])
                if len(hard) > 0:
                    clickRange(win=self.captain, box=hard[0])
        
        invite = find(image=img, templ=images['captain1'])
        if len(invite):
            print('invite')
            clickRange(win=self.captain, box=(190, 130, 40, 20))
            sleep(0.3, 0.5)
            clickRange(win=self.captain, box=invite[0])
            sleep(0.5, 0.6)

        acceptInvite = find(win=self.teammate, templ=images['accept_invite'])
        if len(acceptInvite) > 0:
            clickRange(win=self.teammate, box=acceptInvite[0])

        defaultInvite = find(image=img, tampl=images['confirm'])
        if len(defaultInvite) > 0:
            clickRange(win=self.teammate, box=defaultInvite[0])
        
        return False



    def hasStarted(self):
        if not has(win=self.captain, templ=images['is_in_scene']):
            return True
        
        while 1:
            img = capture(self.captain)
            exp = find(image=img, templ=images['exp'])
            if len(exp) > 0:

        return False


    def hasEnded(self):
        pass


    def hasExited(self):
        pass


states = [
    'inEntry',
    'inScene',
    'inFighting'
]

transitions = [
    {
        'trigger': 'enter',
        'source': 'inEntry',
        'dest': 'inScene',
        'conditions': 'hasEntered'
    }, {
        'trigger': 'search',
        'source': 'inScene',
        'dest': 'inFighting',
        'conditions': 'hasStarted'
    }, {
        'trigger': 'endFight',
        'source': 'inFighting',
        'dest': 'inScene',
        'conditions': 'hasEnded'
    }, {
        'trigger': 'exitScene',
        'source': 'inScene',
        'dest': 'inEntry',
        'conditions': 'hasExited'
    }
]

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
    quitScript()

print('队长是', captain)

g = Gouliang(captain, teammate)
machine = Machine(model=g, states=states,
                  transitions=transitions, initial='inEntry')


def loop():
    print('in loop')
    if g.state == 'inEntry':
        print('in entering')
        g.enter()

    if g.state == 'inScene':
        if not g.search():
            g.exitScene()

    if g.state == 'inFighting':
        g.endFight()


if __name__ == '__main__':
    try:
        while 1:
            loop()
    except KeyboardInterrupt:
        print('quit')
