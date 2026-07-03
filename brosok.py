from translator import *
from random import randint
from propython import pywrite
from players import *

def brosok(obj, base, lang, parameters, result1, final_num, points_list, w, Human, Computer):
    if len(parameters)==6:
        parameter, snakes, lsnakes, ladders, lladders, ssnake=parameters
    else:
        parameter, snakes, lsnakes, ladders, lladders=parameters
        ssnake=[100]
    isdouble=False
    isteleportation=False
    if obj.status==5 and obj.play!=False:
        if isinstance(obj, Human):
            while True:
                enter=input(f'[{obj.name}] {translator('Enter: ', lang)}')
                enter=enter.lower().strip()
                if lang=='ru':
                    enter=translator(enter, 'en1')
                match enter:
                    case 'teleport':
                        if obj.money_teleport==0:
                            print(translator('NO', lang))
                            isteleportation=False
                        else:
                            while True:
                                print(translator('TELEPORTATION 🌀', lang))
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
                            print(translator('DOUBLE ✖️', lang))
                            obj.money_double=0
                            obj.moneys-=1
                            isdouble=True
                    case 'rocket':
                        if obj.money_rocket==0:
                            print(translator('NO', lang))
                        elif obj.level+10>=parameter:
                            print(translator('NO', lang))
                        else:
                            print(translator('ROCKET   +10 🚀', lang))
                            obj.level=obj.rocket()
                    case 'ice':
                        if obj.money_ice==0:
                            print(translator('NO', lang))
                        else:
                            while True:
                                print(translator('ICE 🧊', lang))
                                da_blin=input(translator('Choose player to freeze: ', lang))
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
            elif obj.level in ladders:
                print('🪜')
                obj.level+=6
                print(obj.level)
            elif obj.level in lladders:
                print('🪜🪜')
                obj.level+=12
                print(obj.level)
            else:
                print(obj.level)
        else:
            print(obj.level)
        spisok2_result=(obj.level, obj.status)
    elif obj.play==False:
        print(f'{obj.name} {translator('is frozen!', lang)}')
        spisok2_result=(obj.level, obj.status)
    else:
        spisok2_result=(obj.level, obj.status)
    return spisok2_result