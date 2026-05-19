rutranslate={
    'Error!!!': 'Ошибка!!!',
    'COMPUTER1': 'КОМПЬЮТЕР1',
    'COMPUTER2': 'КОМПЬЮТЕР2',
    'COMPUTER3': 'КОМПЬЮТЕР3',
    'Enter name: ': 'Введите имя: ',
    'Snakes and Stairs': 'Змеи и Лестницы',
    'Creator: Abdyrahym Begenjov': 'Создатель: Абдырахым Бегенджов',
    'Enter to start game: ': 'Нажмите, чтобы начать игру: ',
    'Loading...': 'Загрузка...',
    'Enter number of the players: ': 'Введите количество игроков: ',
    'Parametrs of game: Easy (50), Normal (75), Hard (100)': 'Параметры игры: Лёгкий (50), Нормальный (75), Сложный (100)',
    'Enter the parametr of game: ': 'Введите параметр игры: ',
    'Easy': 'Лёгкий',
    'Normal': 'Нормальный',
    'Hard': 'Сложный',
    'Player 1': 'Игрок 1',
    'Player 2': 'Игрок 2',
    'Player 3': 'Игрок 3',
    'Player 4': 'Игрок 4',
    'Moment of Truth 🥁': 'Момент истины 🥁',
    'Enter: ': 'Введите: ',
    'First Winner': 'Первый победитель',
    'Second Winner': 'Второй победитель',
    'Third Winner': 'Третий победитель',
    'Forth Winner': 'Четвертый победитель',
    'teleport': 'телепортация',
    'TELEPORTATION': 'ТЕЛЕПОРТАЦИЯ',
    'Choose player for teleportation: ': 'Выберите игрока для телепортации: ',
    'double': 'удвоение',
    'DOUBLE': 'УДВОЙНОЕ',
    'rocket': 'ракета',
    'NO': 'НЕТ',
    'ROCKET   +10': 'РАКЕТА   +10',
    'ice': 'лёд',
    'Choose player for ice: ': 'Выберите игрока для льда: ',
    'ICE:': 'ЛЁД:',
    'Generate: ': 'Сгенерировать: ',
    'Number is bigger than parametr': 'Число больше параметра',
    'Long': 'Длинная',
    'Dangerous': 'Опасная',
    'is iced!': ' заморожен!',
    'WINNER': 'ПОБЕДИТЕЛЬ',
    'ROUND-UP': 'ВТОРОЕ МЕСТО',
    'BRONZE MEDALIST': 'БРОНЗОВЫЙ ПРИЗЁР',
    'LOSER': 'ЛУЗЕР',
    'Enter to exit: ': 'Введите для выхода: ',
    'Let\'s Go!!!': 'Начнём!!!',
    'Don\'t write your name!!!': 'Не пиши своё имя!!!'
             }


entranslate={j: i for i, j in rutranslate.items()}


def translator(word, language):
    match language:
        case 'en':
            return word
        case 'en1':
            if word not in entranslate:
                return 'Error!!!'
            return entranslate[word]
        case 'ru':
            return rutranslate[word]
        case _:
            return '???'