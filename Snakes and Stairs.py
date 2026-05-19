from random import randint
from time import sleep
from translator import *

while True:
    print('English  |  Русский')
    l=input()
    l=l.title().strip()
    match l:
        case 'English':
            lan='en'
            break
        case 'Русский':
            lan='ru'
            break
        case _:
            continue

p=[translator('Player 2', lan), translator('Player 3', lan), translator('Player 4', lan)]
c=[translator('COMPUTER1', lan), translator('COMPUTER2', lan), translator('COMPUTER3', lan)]

def game():
    name=input(f'[{p[0]}] {translator('Enter name: ', lan)}')
    p.pop(0)
    if name =='':
        name=c[0]
        c.pop(0)
        return name
    return name

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
    def teleport(self, obj1):
        result=self.level
        self.level=obj1.level
        obj1.level=result
        self.money_teleport=0
        return self.level, obj1.level
    def rocket(self):
        self.level+=10
        self.money_rocket=0
        return self.level

class Computer(Player):
    pass

def ice(obj):
    obj.play=False
    return obj.play
def double(num):
    return num*2

print(translator('Snakes and Stairs', lan))
print(f'{translator('Creator: Abdyrahym Begenjov', lan)}    (GitHub: abdyrahym-begenjov)')
start=input(translator('Enter to start game: ', lan))
print(translator('Loading...', lan))
sleep(2)
print('_'*100)

while True:
    count=input(translator('Enter number of the players: ', lan))
    if count in ('2', '3', '4'):
        count=int(count)
        break
    else:
        print(translator('Error!!!', lan))

snakes, lsnakes, stairs, lstairs, ssnake = [], [], [], [], []
print(translator('Parametrs of game: Easy (50), Normal (75), Hard (100)', lan))

while True:
    parametr=input(translator('Enter the parametr of game: ', lan))
    parametr=parametr.title().strip()
    if lan=='ru':
        parametr=translator(parametr, 'en1')
    match parametr:
        case 'Easy':
            parametr=50
            snakes=[13, 31]
            lsnakes=[47]
            stairs=[8, 38]
            lstairs=[22]
            break
        case 'Normal':
            parametr=75
            snakes=[25, 36, 49]
            lsnakes=[73, 68]
            stairs=[20, 38, 57]
            lstairs=[3, 12]
            break
        case 'Hard':
            parametr=100
            snakes=[24, 64, 63, 62]
            lsnakes=[13, 49, 80]
            stairs=[4, 32, 70, 61]
            lstairs=[15, 55, 87]
            ssnake=[95]
            break
        case _:
            print(translator('Error!!!', lan))

lst1=[]
while True:
    Player1=input(f'[{translator('Player 1', lan)}] {translator('Enter name: ', lan)}')
    if Player1!='':
        lst1.append(Player1)
        break
    else:
        print(translator('Error!!!', lan))

for i in range(count-1):
    x=game()
    lst1.append(x)

while True:
    lst=[]
    for i in lst1:
        move=randint(1, 6)
        lst.append((i, move))
    lst.sort(key=lambda x: x[1], reverse=True)    
    result=list(map(lambda x: x[1], lst))
    nr, r=[], []
    for i in result:
        if i not in nr:
            nr.append(i)
        else:
            r.append(i)
    if r==[]:
        print(translator('Moment of Truth 🥁', lan))
        match count:
            case 2:
                sleep(2)
            case 3:
                sleep(4)
            case 4:
                sleep(6)
        result=[f'{i}: {c}' for i, c in lst]
        text=', '.join(result)
        print(text)
        break
    else:
        continue

new_lst=list(map(lambda x: x[0], lst))
result1=[]
for i in new_lst:
    if i in [translator('COMPUTER1', lan), translator('COMPUTER2', lan), translator('COMPUTER3', lan)]:
        result1.append(Computer(i))
    else:
        result1.append(Human(i))

for n, i in enumerate(result1, 1):
    print(f'{n}) {i.name}')

start1=input(translator('Enter to start game: ', lan))
print(translator('Let\'s Go!!!', lan))
w=[translator('First Winner', lan), translator('Second Winner', lan), translator('Third Winner', lan), translator('Forth Winner', lan)]
final_num=[1, 2, 3, 4]

def brosok(obj):
    isdouble=False
    isteleportation=False
    if obj.status==5 and obj.play!=False:
        if isinstance(obj, Human):
            while True:
                enter=input(f'[{obj.name}] {translator('Enter: ', lan)}')
                if lan=='ru':
                    enter=translator(enter, 'en1')
                match enter:
                    case 'teleport':
                        if obj.money_teleport==0:
                            print(translator('NO', lan))
                            isteleportation=False
                        else:
                            while True:
                                print(translator('TELEPORTATION', lan))
                                da_blin=input(translator('Choose player for teleportation: ', lan))
                                if da_blin==obj.name:
                                    print(translator('Don\'t write your name!!!', lan))
                                elif da_blin in [i.name for i in result1]:
                                    print(f'{obj.name} --> {da_blin}')
                                    for i in result1:
                                        if da_blin==i.name:
                                            obj.level, i.level=obj.teleport(i)
                                    break
                                else:
                                    print(translator('Error!!!', lan))
                            isteleportation=True
                        break
                    case 'double':
                        if obj.money_double==0:
                            print(translator('NO', lan))
                            isdouble=False
                        else:
                            print(translator('DOUBLE', lan))
                            obj.money_double=0
                            isdouble=True
                    case 'rocket':
                        if obj.money_rocket==0:
                            print(translator('NO', lan))
                        elif obj.level+10>=parametr:
                            print(translator('NO', lan))
                        else:
                            print(translator('ROCKET   +10', lan))
                            obj.level=obj.rocket()
                    case 'ice':
                        if obj.money_ice==0:
                            print(translator('NO', lan))
                        else:
                            while True:
                                da_blin=input(translator('Choose player for ice: ', lan))
                                if da_blin==obj.name:
                                    print(translator('Don\'t write your name!!!', lan))
                                elif da_blin in [i.name for i in result1]:
                                    print(f'{translator('ICE:', lan)} {da_blin}')
                                    for i in result1:
                                        if da_blin==i.name:
                                            i.play=ice(i)
                                    obj.money_ice=0
                                    break
                                else:
                                    print(translator('Error!!!', lan))
                    case _:
                        break
        if isteleportation==False:
            if isinstance(obj, Computer):
                print(f'[{obj.name}] {translator('Generate: ', lan)}')
            num=randint(1, 6)
            if isdouble==True:
                print(f'{num}x2')
                num=double(num)
            print(f'{num}')
            obj.level+=num
            if obj.level==parametr:
                print(obj.level)
                obj.status=final_num[0]
                print(w[0])
                final_num.pop(0)
                w.pop(0)
            elif obj.level>parametr:
                print(translator('Number is bigger than parametr', lan))
                obj.level-=num
                print(obj.level)
            elif obj.level in snakes:
                print('🐍')
                obj.level-=6
                print(obj.level)
            elif obj.level in lsnakes:
                print('🐍🐍')
                obj.level-=12
                print(obj.level)
            elif obj.level in ssnake:
                print(f'{translator('Dangerous', lan)} 🐍')
                obj.level-=60
                print(obj.level)
            elif obj.level in stairs:
                print('🪜')
                obj.level+=6
                print(obj.level)
            elif obj.level in lstairs:
                print('🪜🪜')
                obj.level+=12
                print(obj.level)
            else:
                print(obj.level)
        else:
            print(obj.level)
        spisok2_result=(obj.level, obj.status)
    elif obj.play==False:
        print(f'{obj.name} {translator('is iced!', lan)}')
        spisok2_result=(obj.level, obj.status)
    else:
        spisok2_result=(obj.level, obj.status)
    return spisok2_result

while True:
    for player in result1:
        player.level, player.status=brosok(player)
        player.play=True
    spisok=[]
    for player in result1:
        spisok.append((player.name, player.level, player.status))
    spisok.sort(key=lambda x: x[2], reverse=False)
    spisok1=list(map(lambda x: x[0], spisok))
    spisok2=list(map(lambda x: x[2], spisok))
    if 1 in spisok2 and count==2:
        print(f'1) {spisok1[0]} - {translator('WINNER', lan)} 😎🏆')
        print(f'2) {spisok1[1]} - {translator('LOSER', lan)} 😫')
        break
    elif 1 in spisok2 and 2 in spisok2 and count==3:
        print(f'1) {spisok1[0]} - {translator('WINNER', lan)} 😎🏆')
        print(f'2) {spisok1[1]} - {translator('ROUND-UP', lan)} 😀')
        print(f'3) {spisok1[2]} - {translator('LOSER', lan)} 😫')
        break
    elif 1 in spisok2 and 2 in spisok2 and 3 in spisok2 and count==4:
        print(f'1) {spisok1[0]} - {translator('WINNER', lan)} 😎🏆')
        print(f'2) {spisok1[1]} - {translator('ROUND-UP', lan)} 😀')
        print(f'3) {spisok1[2]} - {translator('BRONZE MEDALIST', lan)} 😐')
        print(f'4) {spisok1[3]} - {translator('LOSER', lan)} 😫')
        break

end=input(translator('Enter to exit: ', lan))