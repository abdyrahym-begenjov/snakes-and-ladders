class Player:
    def __init__(self, name):
        self.name=name
        self.level=0
        self.status=5
        self.play=True

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.money_ice=1
        self.money_rocket=1
        self.money_teleport=1
        self.money_double=1
        self.moneys=4
    def teleport(self, obj1):
        result=self.level
        self.level=obj1.level
        obj1.level=result
        self.money_teleport=0
        self.moneys-=1
        return self.level, obj1.level
    def rocket(self):
        self.level+=10
        self.money_rocket=0
        self.moneys-=1
        return self.level

class Computer(Player):
    pass

def ice(obj):
    obj.play=False
    return obj.play
def double(num):
    return num*2