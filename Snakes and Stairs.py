from random import randint

c='COMPUTER'

class Player:
    def __init__(self, name):
        self.name=name
        self.level=0
        self.status=5
    def __iadd__(self, number):
        self.level+=number
        return self.level
    def __isub__(self, number):
        self.level-=number
        return self.level
    
class Computer:
    def __init__(self, name):
        self.name=name
        self.level=0
        self.status=5
    def __iadd__(self, number):
        self.level+=number
        return self.level
    def __isub__(self, number):
        self.level-=number
        return self.level

parametr=50
snakes=[13, 31]
lsnakes=[47]
stairs=[8, 38]
lstairs=[22]

while True:
    Player1=input('[Player 1] Enter name: ')
    if Player1!='':
        break
    else:
        print('Error!!!')

Player2=input('[Player 2] Enter name: ')
if Player2 =='':
    Player2=c

while True:
    u1=randint(1, 6)
    u2=randint(1, 6)
    lst=[(Player1, u1), (Player2, u2)]
    lst.sort(key=lambda x: x[1], reverse=True)
    result=list(map(lambda x: x[1], lst))
    nr, r=[], []
    for i in result:
        if i not in nr:
            nr.append(i)
        else:
            r.append(i)
    if r==[]:
        print(f'{Player1}: {u1}, {Player2}: {u2}')
        break
    else:
        continue

new_lst=list(map(lambda x: x[0], lst))
result1=[]
for i in new_lst:
    if i=='COMPUTER':
        result1.append(Computer(i))
    else:
        result1.append(Player(i))

P1, P2=result1

for n, i in enumerate(result1, 1):
    print(f'{n}) {i.name}')

start1=input('Enter to start game: ')
w='Winner'
final_num=[1, 2]
def brosok(obj):
    if obj.status==5:
        if isinstance(obj, Player):
            enter=input(f'[{obj.name}] Enter: ')
        if isinstance(obj, Computer):
            print(f'[{obj.name}] Generate: ')
        num=randint(1, 6)
        print(f'{num}')
        obj.level+=num
        if obj.level==parametr:
            obj.status=final_num[0]
            print(w)
            final_num.pop(0)
        elif obj.level>parametr:
            print('Number is bigger than parametr')
            obj.level-=num
        elif obj.level in snakes:
            print('🐍')
            obj.level-=6
        elif obj.level in lsnakes:
            print('Long 🐍')
            obj.level-=12
        elif obj.level in stairs:
            print('⬆️')
            obj.level+=6
        elif obj.level in lstairs:
            print('Long ⬆️')
            obj.level+=12
            print(obj.level)
        else:
            print(obj.level)
        spisok2_result=(obj.level, obj.status)
    else:
        spisok2_result=(obj.level, obj.status)
    return spisok2_result

while True:
    P1.level, P1.status=brosok(P1)
    P2.level, P2.status=brosok(P2)
    spisok=[(P1.name, P1.level, P1.status), (P2.name, P2.level, P2.status)]
    spisok.sort(key=lambda x: x[2], reverse=False)
    spisok1=list(map(lambda x: x[0], spisok))
    spisok2=list(map(lambda x: x[2], spisok))
    if 1 in spisok2:
        print(f'1) {spisok1[0]} - WINNER 😎🏆')
        print(f'2) {spisok1[1]} - LOSER 😫')
        break