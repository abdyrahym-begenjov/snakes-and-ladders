rutranslate={
    'Error!!!': 'Ошибка!!!',
    'COMPUTER1': 'КОМПЬЮТЕР1',
    'COMPUTER2': 'КОМПЬЮТЕР2',
    'COMPUTER3': 'КОМПЬЮТЕР3',
    'Enter name: ': 'Введите имя: ',
    'Snakes and Ladders': 'Змеи и Лестницы',
    'Creator: Abdyrahym Begenjov': 'Создатель: Абдырахым Бегенджов',
    'Enter to start game: ': 'Нажмите, чтобы начать игру: ',
    'Loading...': 'Загрузка...',
    'Enter number of the players: ': 'Введите количество игроков: ',
    'Parameters of game: Easy (50), Normal (75), Hard (100)': 'Параметры игры: Лёгкий (50), Нормальный (75), Сложный (100)',
    'Enter the parameter of game: ': 'Введите параметр игры: ',
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
    'TELEPORTATION 🌀': 'ТЕЛЕПОРТАЦИЯ 🌀',
    'Choose player for teleportation: ': 'Выберите игрока для телепортации: ',
    'double': 'удвоение',
    'DOUBLE ✖️': 'УДВОЙНОЕ ✖️',
    'rocket': 'ракета',
    'NO': 'НЕТ',
    'ROCKET   +10 🚀': 'РАКЕТА   +10 🚀',
    'ICE 🧊': 'ЛЁД 🧊',
    'ice': 'лёд',
    'Choose player for ice: ': 'Выберите игрока для льда: ',
    'ICE:': 'ЛЁД:',
    'Generate: ': 'Сгенерировать: ',
    'Number is bigger than parameter': 'Число больше параметра',
    'Long': 'Длинная',
    'Dangerous': 'Опасная',
    'is iced!': ' заморожен!',
    'WINNER': 'ПОБЕДИТЕЛЬ',
    'ROUND-UP': 'ВТОРОЕ МЕСТО',
    'BRONZE MEDALIST': 'БРОНЗОВЫЙ ПРИЗЁР',
    'LOSER': 'ЛУЗЕР',
    'Enter to exit: ': 'Введите для выхода: ',
    'Let\'s Go!!!': 'Начнём!!!',
    'Don\'t write your name!!!': 'Не пиши своё имя!!!',
    'Enter to exit mode: ': 'Войдите в режим выхода: ',
    'Game      Rules      Highscores      Settings      Exit': 'Игра      Правила      Рекорды      Настройки      Выход',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Do you want to change language (Enter \"Language\"): ': 'Хотите ли вы изменить язык (введите \"Язык\"): ',
    'Do you want to exit (\"Yes\" or \"No\"): ': 'Вы хотите завершить (\"Да\" или \"Нет\"): ',
    'Goodbye!!!': 'До свидания!!',
    'Language': 'Язык',
    'No': 'Нет',
    'Game': 'Игра',
    'Rules': 'Правила',
    'Highscores': 'Рекорды',
    'Settings': 'Настройки',
    'Exit': 'Выход',
    'NAME |': 'ИМЯ |',
    'POINTS': 'БАЛЛЫ',
    'LEADERBOARD:': 'ЛИДЕРБОРД:', 
    'Since you didn\'t use any abilities, you get double points': 'Поскольку вы не использовали никаких способностей, вы получаете двойные очки'
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