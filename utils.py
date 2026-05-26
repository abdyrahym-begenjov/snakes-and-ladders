from platform import system
from subprocess import run
from propython import pywrite

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_lang(data):
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