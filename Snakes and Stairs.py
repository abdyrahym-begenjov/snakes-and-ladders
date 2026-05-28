from random import randint
from time import sleep
from translator import *
from propython import pyread, pywrite
from players import *
from utils import *

base=pyread('base.json')
data=pyread('data.json')

lang=data['language']

if lang=='':
    lang=enter_lang(data)
    clear_screen()

while True:
    print(translator('Snakes and Stairs', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}    (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Rules      Highscores      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=mode.title().strip()
    clear_screen()
    if lang=='ru':
        mode=translator(mode, 'en1')
    match mode:
        case 'Game':
            p=[translator('Player 2', lang), translator('Player 3', lang), translator('Player 4', lang)]
            c=[translator('COMPUTER1', lang), translator('COMPUTER2', lang), translator('COMPUTER3', lang)]

            def game():
                name=input(f'[{p[0]}] {translator('Enter name: ', lang)}')
                p.pop(0)
                if name=='':
                    name=c[0]
                    c.pop(0)
                if name not in base:
                    if name.startswith('КОМПЬЮТЕР'):
                        if translator(name, 'en1') in base:
                            pass
                        else:
                            base[translator(name, 'en1')]=0
                    else:
                        base[name]=0
                    pywrite('base.json', base)
                return name


            
            start=input(translator('Enter to start game: ', lang))
            print(translator('Loading...', lang))
            sleep(2)
            clear_screen()
            while True:
                count=input(translator('Enter number of the players: ', lang))
                if count in ('2', '3', '4'):
                    try:
                        count=int(count)
                        break
                    except ValueError:
                        print(translator('Error!!!', lang))
                else:
                    print(translator('Error!!!', lang))

            snakes, lsnakes, stairs, lstairs, ssnake = [], [], [], [], []
            print(translator('Parameters of game: Easy (50), Normal (75), Hard (100)', lang))

            while True:
                parameter=input(translator('Enter the parameter of game: ', lang))
                parameter=parameter.title().strip()
                if lang=='ru':
                    parameter=translator(parameter, 'en1')
                match parameter:
                    case 'Easy':
                        parameter=50
                        snakes=[13, 31]
                        lsnakes=[47]
                        stairs=[8, 38]
                        lstairs=[22]
                        break
                    case 'Normal':
                        parameter=75
                        snakes=[25, 36, 49]
                        lsnakes=[73, 68]
                        stairs=[20, 38, 57]
                        lstairs=[3, 12]
                        break
                    case 'Hard':
                        parameter=100
                        snakes=[24, 64, 63, 62]
                        lsnakes=[13, 49, 80]
                        stairs=[4, 32, 70, 61]
                        lstairs=[15, 55, 87]
                        ssnake=[95]
                        break
                    case _:
                        print(translator('Error!!!', lang))

            lst1=[]
            while True:
                Player1=input(f'[{translator('Player 1', lang)}] {translator('Enter name: ', lang)}')
                if Player1!='':
                    lst1.append(Player1)
                    if Player1 not in base:
                        base[Player1]=0
                        pywrite('base.json', base)
                    break
                else:
                    print(translator('Error!!!', lang))

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
                    print(translator('Moment of Truth 🥁', lang))
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
                if i in [translator('COMPUTER1', lang), translator('COMPUTER2', lang), translator('COMPUTER3', lang)]:
                    result1.append(Computer(i))
                else:
                    result1.append(Human(i))

            for n, i in enumerate(result1, 1):
                print(f'{n}) {i.name}')

            start1=input(translator('Enter to start game: ', lang))
            clear_screen()
            print(translator('Let\'s Go!!!', lang))
            w=[translator('First Winner', lang), translator('Second Winner', lang), translator('Third Winner', lang), translator('Forth Winner', lang)]
            points_list=[3, 2, 1, 0]
            final_num=[1, 2, 3, 4]

            def brosok(obj):
                isdouble=False
                isteleportation=False
                if obj.status==5 and obj.play!=False:
                    if isinstance(obj, Human):
                        while True:
                            enter=input(f'[{obj.name}] {translator('Enter: ', lang)}')
                            if lang=='ru':
                                enter=translator(enter, 'en1')
                            match enter:
                                case 'teleport':
                                    if obj.money_teleport==0:
                                        print(translator('NO', lang))
                                        isteleportation=False
                                    else:
                                        while True:
                                            print(translator('TELEPORTATION', lang))
                                            da_blin=input(translator('Choose player for teleportation: ', lang))
                                            if da_blin==obj.name:
                                                print(translator('Don\'t write your name!!!', lang))
                                            elif da_blin in [i.name for i in result1]:
                                                print(f'{obj.name} --> {da_blin}')
                                                for i in result1:
                                                    if da_blin==i.name:
                                                        obj.level, i.level=obj.teleport(i)
                                                break
                                            else:
                                                print(translator('Error!!!', lang))
                                        isteleportation=True
                                    break
                                case 'double':
                                    if obj.money_double==0:
                                        print(translator('NO', lang))
                                        isdouble=False
                                    else:
                                        print(translator('DOUBLE', lang))
                                        obj.money_double=0
                                        obj.moneys-=1
                                        isdouble=True
                                case 'rocket':
                                    if obj.money_rocket==0:
                                        print(translator('NO', lang))
                                    elif obj.level+10>=parameter:
                                        print(translator('NO', lang))
                                    else:
                                        print(translator('ROCKET   +10', lang))
                                        obj.level=obj.rocket()
                                case 'ice':
                                    if obj.money_ice==0:
                                        print(translator('NO', lang))
                                    else:
                                        while True:
                                            da_blin=input(translator('Choose player for ice: ', lang))
                                            if da_blin==obj.name:
                                                print(translator('Don\'t write your name!!!', lang))
                                            elif da_blin in [i.name for i in result1]:
                                                print(f'{translator('ICE:', lang)} {da_blin}')
                                                for i in result1:
                                                    if da_blin==i.name:
                                                        i.play=ice(i)
                                                obj.money_ice=0
                                                obj.moneys-=1
                                                break
                                            else:
                                                print(translator('Error!!!', lang))
                                case _:
                                    break
                    if isteleportation==False:
                        if isinstance(obj, Computer):
                            print(f'[{obj.name}] {translator('Generate: ', lang)}')
                        num=randint(1, 6)
                        if isdouble==True:
                            print(f'{num}x2')
                            num=double(num)
                        print(f'{num}')
                        obj.level+=num
                        if obj.level==parameter:
                            print(obj.level)
                            obj.status=final_num[0]
                            print(w[0])
                            final_num.pop(0)
                            w.pop(0)
                            point=points_list.pop(0)
                            if isinstance(obj, Human) and obj.moneys==4:
                                print(translator('Since you didn\'t use any abilities, you get double points', lang))
                                point*=2
                            if obj.name.startswith('КОМПЬЮТЕР'):
                                base[translator(obj.name, 'en1')]+=point
                            else:
                                base[obj.name]+=point
                            pywrite('base.json', base)
                        elif obj.level>parameter:
                            print(translator('Number is bigger than parameter', lang))
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
                            print(f'{translator('Dangerous', lang)} 🐍')
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
                    print(f'{obj.name} {translator('is iced!', lang)}')
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
                    print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆')
                    print(f'2) {spisok1[1]} - {translator('LOSER', lang)} 😫')
                    break
                elif 1 in spisok2 and 2 in spisok2 and count==3:
                    print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆')
                    print(f'2) {spisok1[1]} - {translator('ROUND-UP', lang)} 😀')
                    print(f'3) {spisok1[2]} - {translator('LOSER', lang)} 😫')
                    break
                elif 1 in spisok2 and 2 in spisok2 and 3 in spisok2 and count==4:
                    print(f'1) {spisok1[0]} - {translator('WINNER', lang)} 😎🏆')
                    print(f'2) {spisok1[1]} - {translator('ROUND-UP', lang)} 😀')
                    print(f'3) {spisok1[2]} - {translator('BRONZE MEDALIST', lang)} 😐')
                    print(f'4) {spisok1[3]} - {translator('LOSER', lang)} 😫')
                    break

            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Rules':
            if lang=='ru':
                rules=pyread('ru_rules.txt')
            else:
                rules=pyread('en_rules.txt')
            print(rules)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Highscores':
            print(translator('LEADERBOARD:', lang))
            base=dict(sorted(base.items(), key=lambda x: x[1], reverse=True))
            for i, j in base.items():
                if i.startswith('COMPUTER') and lang=='ru':
                    i=translator(i, 'ru')
                print(f'{i}: {j}')
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Settings':
            while True:
                print(f'{translator('Language', lang)}: {data['language']}')
                change=input(translator('Do you want to change language (Enter \"Language\"): ', lang))
                change=change.title().strip()
                if lang=='ru':
                    change=translator(change, 'en1')
                match change:
                    case 'Language':
                        lang=enter_lang(data)
                        clear_screen()
                    case _:
                        break
            clear_screen()

        case 'Exit':
            exit_confirm=input(translator('Do you want to exit (\"Yes\" or \"No\"): ', lang))
            exit_confirm=exit_confirm.title().strip()
            if lang=='ru':
                exit_confirm=translator(exit_confirm, 'en1')
            if exit_confirm=='No':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        
        case _:
            clear_screen()