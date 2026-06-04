from random import randint
from time import sleep
from translator import *
from propython import pyread, pywrite
from players import *
from utils import *
from brosok import *

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
    mode=new_word(mode, lang)
    clear_screen()
    match mode:
        case 'Game':
            p=[translator('Player 2', lang), translator('Player 3', lang), translator('Player 4', lang)]
            c=[translator('COMPUTER1', lang), translator('COMPUTER2', lang), translator('COMPUTER3', lang)]
            
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

            print(translator('Parameters of game: Easy (50), Normal (75), Hard (100)', lang))

            parameters=selection_of_parameters(lang)

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
                x=game(p, c, base, lang)
                lst1.append(x)

            result1=selection_of_order(lst1, count, lang, Computer, Human)

            for n, i in enumerate(result1, 1):
                print(f'{n}) {i.name}')

            start1=input(translator('Enter to start game: ', lang))
            clear_screen()
            print(translator('Let\'s Go!!!', lang))
            w=[translator('First Winner', lang), translator('Second Winner', lang), translator('Third Winner', lang), translator('Forth Winner', lang)]
            points_list=[3, 2, 1, 0]
            final_num=[1, 2, 3, 4]

            while True:
                for player in result1:
                    player.level, player.status=brosok(player, base, lang, parameters, result1, final_num, points_list, w, Human, Computer)
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
            draw_leaderboard(base, lang)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Settings':
            while True:
                print(f'{translator('Language', lang)}: {data['language']}')
                change=input(translator('Do you want to change language (Enter \"Language\"): ', lang))
                change=new_word(change, lang)
                match change:
                    case 'Language':
                        lang=enter_lang(data)
                        clear_screen()
                    case _:
                        break
            clear_screen()

        case 'Exit':
            exit_confirm=input(translator('Do you want to exit (\"Yes\" or \"No\"): ', lang))
            exit_confirm=new_word(exit_confirm, lang)
            if exit_confirm=='No':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        
        case _:
            clear_screen()