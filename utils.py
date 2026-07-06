from platform import system
from subprocess import run
from propython import pywrite
from translator import *
from random import randint
from time import sleep

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_lang(data):
    clear_screen()
    while True:
        print('English |  Русский')
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        if chosen_language=='English' or chosen_language=='Русский':
            break
        else:
            clear_screen()

    match chosen_language:
        case 'Русский':
            lang='ru'
        case 'English':
            lang='en'
    data['language']=lang
    pywrite('data.json', data)
    return lang

def enter_name(data, base, lang):
    clear_screen()
    while True:
        name=input(translator('Enter your name: ', lang))
        name=name.strip()
        if name=='':
            clear_screen()
            print(translator('Error!!!', lang))
        elif len(name)>16:
            clear_screen()
            print(translator('The name must not exceed 16 characters', lang))
        else:
            data['name']=name
            pywrite('data.json', data)
            if name not in base:
                base[name]=0
                pywrite('base.json', base)
            return name

def game(p, c, lst1, base, lang):
    while True:
        name=input(f'[{p[0]}] {translator('Enter name: ', lang)}')
        if name in lst1:
            print(translator('This name is already taken', lang))
        elif len(name)>16:
            print(translator('The name must not exceed 16 characters', lang))
        else:
            if name=='':
                name=c[0]
                c.pop(0)
            p.pop(0)
            break
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

def new_word(word, lang):
    word=word.strip().title()
    if lang=='ru':
        word=translator(word, 'en1')
    return word

def selection_of_order(lst1, game_count, lang, Computer, Human):
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
            match game_count:
                case 2:
                    sleep(2)
                case 3:
                    sleep(4)
                case 4:
                    sleep(6)
            clear_screen()
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
    return result1

def selection_of_parameters(lang):
    while True:
        parameters=input(translator('Enter the parameter of game: ', lang))
        parameters=new_word(parameters, lang)
        match parameters:
            case 'Easy':
                parameters=[50, [13, 31], [47], [8, 38], [22]]
                break
            case 'Normal':
                parameters=[75, [25, 36, 49], [73, 68], [20, 38, 57], [3, 12]]
                break
            case 'Hard':
                parameters=[100, [24, 64, 63, 62], [13, 49, 80], [4, 32, 70, 61], [15, 55, 87], [95]]
                break
            case _:
                print(translator('Error!!!', lang))
    return parameters

def draw_leaderboard(base, lang):
    print(translator('LEADERBOARD:', lang))
    base=list(base.items())
    base.sort(key=lambda x: x[1], reverse=True)
    base=dict(base)

    line1=f'|{translator('NAME |', lang):>18} {translator('POINTS', lang):<16}|'
    line='-'*len(line1)
    print(line)
    print(line1)
    print(line)

    for i, j in base.items():
        name=translator(i, lang) if i.startswith('COMPUTER') else i
        a=str(j)
        name1=f'{name} |'
    
        line2=f'|{name1:>18} {a:<16}|'
        print(line2)
        print(line)