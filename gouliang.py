from transitions import Machine
from utils import *
import sys


class Gouliang(object):
    def __init__(self, captain, teammate):
        self.captain = captain
        self.teammate = teammate

    def hasEntered(self):
        img = capture(self.captain)
        
        pass


    def hasStarted(self):
        pass


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
                  transitions=transitions, initial='creating_group')


def loop():
    if g.state == 'inEntry':
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
