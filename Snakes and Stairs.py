from random import randint
from time import sleep
c=['COMPUTER1', 'COMPUTER2', 'COMPUTER3']

def game(info):
    name=input(f'[{info}] Enter name: ')
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

print('Snakes and Stairs')
print('Creator: Abdyrahym Begenjov    (GitHub: abdyrahym-begenjov)')
start=input('Enter to start game: ', )
print('Loading...', )
sleep(2)
print('_'*100)

while True:
    count=input('Enter number of the players: ')
    if count in ('2', '3', '4'):
        count=int(count)
        break
    else:
        print('Error!!!')

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

match count:
    case 2:
        Player2=game('Player 2')
    case 3:
        Player2=game('Player 2')
        Player3=game('Player 3')
    case 4:
        Player2=game('Player 2')
        Player3=game('Player 3')
        Player4=game('Player 4')   

while True:
    match count:
        case 2:
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
                print('Moment of Truth 🥁')
                sleep(2)
                print(f'{Player1}: {u1}, {Player2}: {u2}')
                break
            else:
                continue
        case 3:
            u1=randint(1, 6)
            u2=randint(1, 6)
            u3=randint(1, 6)
            lst=[(Player1, u1), (Player2, u2), (Player3, u3)]
            lst.sort(key=lambda x: x[1], reverse=True)
            result=list(map(lambda x: x[1], lst))
            nr, r=[], []
            for i in result:
                if i not in nr:
                    nr.append(i)
                else:
                    r.append(i)
            if r==[]:
                print('Moment of Truth 🥁')
                sleep(3)
                print(f'{Player1}: {u1}, {Player2}: {u2}, {Player3}: {u3}')
                break
            else:
                continue
        case 4:
            u1=randint(1, 6)
            u2=randint(1, 6)
            u3=randint(1, 6)
            u4=randint(1, 6)
            lst=[(Player1, u1), (Player2, u2), (Player3, u3), (Player4, u4)]
            lst.sort(key=lambda x: x[1], reverse=True)
            result=list(map(lambda x: x[1], lst))
            nr, r=[], []
            for i in result:
                if i not in nr:
                    nr.append(i)
                else:
                    r.append(i)
            if r==[]:
                print('Moment of Truth 🥁')
                sleep(6)
                print(f'{Player1}: {u1}, {Player2}: {u2}, {Player3}: {u3}, {Player4}: {u4}')
                break
            else:
                continue

new_lst=list(map(lambda x: x[0], lst))
result1=[]
for i in new_lst:
    if i in ['COMPUTER1', 'COMPUTER2', 'COMPUTER3']:
        result1.append(Computer(i))
    else:
        result1.append(Player(i))

match count:
    case 2:
        P1, P2=result1
    case 3:
        P1, P2, P3=result1
    case 4:
        P1, P2, P3, P4=result1

for n, i in enumerate(result1, 1):
    print(f'{n}) {i.name}')

start1=input('Enter to start game: ')
print('Let\'s Go!!!')
w=['First Winner', 'Second Winner', 'Third Winner', 'Forth Winner']
final_num=[1, 2, 3, 4]

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
            print(w[0])
            final_num.pop(0)
            w.pop(0)
        elif obj.level>parametr:
            print('Number is bigger than parametr')
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
        spisok2_result=(obj.level, obj.status)
    else:
        spisok2_result=(obj.level, obj.status)
    return spisok2_result

while True:
    P1.level, P1.status=brosok(P1)
    P1.play=True
    match count:
        case 2:
            P2.level, P2.status=brosok(P2)
            P2.play=True
            spisok=[(P1.name, P1.level, P1.status), (P2.name, P2.level, P2.status)]
            spisok.sort(key=lambda x: x[2], reverse=False)
            spisok1=list(map(lambda x: x[0], spisok))
            spisok2=list(map(lambda x: x[2], spisok))
            if 1 in spisok2:
                print(f'1) {spisok1[0]} - WINNER 😎🏆')
                print(f'2) {spisok1[1]} - LOSER 😫')
                break
        case 3:
            P2.level, P2.status=brosok(P2)
            P2.play=True
            P3.level, P3.status=brosok(P3)
            P3.play=True
            spisok=[(P1.name, P1.level, P1.status), (P2.name, P2.level, P2.status), (P3.name, P3.level, P3.status)]
            spisok.sort(key=lambda x: x[2], reverse=False)
            spisok1=list(map(lambda x: x[0], spisok))
            spisok2=list(map(lambda x: x[2], spisok))
            if 1 in spisok2 and 2 in spisok2:
                print(f'1) {spisok1[0]} - WINNER 😎🏆')
                print(f'2) {spisok1[1]} - ROUND-UP 😀')
                print(f'3) {spisok1[2]} - LOSER 😫')
                break
        case 4:
            P2.level, P2.status=brosok(P2)
            P2.play=True
            P3.level, P3.status=brosok(P3)
            P3.play=True
            P4.level, P4.status=brosok(P4)
            P4.play=True
            spisok=[(P1.name, P1.level, P1.status), (P2.name, P2.level, P2.status), (P3.name, P3.level, P3.status), (P4.name, P4.level, P4.status)]
            spisok.sort(key=lambda x: x[2], reverse=False)
            spisok1=list(map(lambda x: x[0], spisok))
            spisok2=list(map(lambda x: x[2], spisok))
            if 1 in spisok2 and 2 in spisok2 and 3 in spisok2:
                print(f'1) {spisok1[0]} - WINNER 😎🏆')
                print(f'2) {spisok1[1]} - ROUND-UP 😀')
                print(f'3) {spisok1[2]} - BRONZE MEDALIST 😐')
                print(f'4) {spisok1[3]} - LOSER 😫')
                break

end=input('Enter to exit: ')