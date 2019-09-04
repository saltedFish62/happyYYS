from transitions import Machine, core


class Matter(object):
    times = 0
    def is_flammable(self): return False

    def is_really_hot(self):
        self.times += 1
        if self.times < 5:
            return False
        else:
            return True


lump = Matter()
machine = Machine(model=lump, states=[
                  'solid', 'liquid', 'gas', 'plasma'], initial="solid")

machine.add_transition('heat', 'solid', 'gas', conditions='is_flammable')
machine.add_transition('heat', 'solid', 'liquid', conditions=['is_really_hot'])

try:
    while 1:
        print(lump.heat())
        print(lump.state)
except core.MachineError as err:
    print(err)

print("quit")
