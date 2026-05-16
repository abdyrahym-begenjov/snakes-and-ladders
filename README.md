# snakes-and-stairs
Snakes and Stairs
# Snakes and Stairs 🐍⬆️
## English
A console implementation of the classic board game "Snakes and Ladders" in Python. The game supports both human and computer opponents.
### 🎮 Game Features
* **Flexible Players**: Supports 2 to 4 players.
* **Computer Opponents**: If you press *Enter* while entering your name, the computer will take your place.
* **Moment of Truth Mechanic**: At the start of the game, the dice are automatically rolled to determine the turn order.
* **Interactive Elements**:
* 🐍 **Snakes**: Knock back 6 squares.
* 🐉 **Long Snakes**: Knock back 12 squares.
* ⬆️ **Ladders**: Move forward 6 squares.
* 🪜 **Long Ladders**: Move forward 12 squares.
* **Game Modes (Difficulty)**: Choose your target score before starting:
   * **Easy**: 50 points
   * **Normal**: 75 points
   * **Hard**: 100 points
If the number rolled exceeds the limit, the player remains in place.
### 🚀 How to run
1. Make sure you have Python 3.10 or higher installed.
2. Download the Snakes and Stairs.py file.
3. Run it via the terminal:
python "Snakes and Stairs.py
### 🛠 Controls
* Enter the number of players (2, 3, or 4).
* Enter names. To add a bot, leave the name field blank.
* During the game, press **Enter** to roll the dice for your character. The bot "rolls" the dice automatically.
## 📝 Description of the second commit (Commit Message)
**Title:** feat: Added player composition selection and the "Moment of Truth" mechanic
**Description:**
* **Multiplayer:** Added the ability to select the number of players (from 2 to 4). Implemented support for bots (COMPUTER1-3) if the name field is left blank.
* **Moment of Truth:** Added an algorithm for determining the turn order at the beginning of the game. The system rolls dice for each player and sorts them in descending order (excluding duplicates by re-rolling).
*  **Movement Logic:** Added Human and Computer classes. Implemented the throw function with processing of special fields (snakes, ladders, overflights).
* **Final Ranking:** Implemented a ranking system (Winner, Runner-up, Loser) based on the number of participants.

# Змейки и Лестницы 🐍⬆️
## Русский
Консольная реализация классической настольной игры «Змеи и лестницы» на Python. Игра поддерживает как живых игроков, так и компьютерных оппонентов.
### 🎮 Особенности игры
 * **Гибкий состав**: Поддержка от 2 до 4 игроков.
 * **Компьютерные оппоненты**: Если при вводе имени нажать *Enter*, место игрока займет компьютер.
 * **Механика «Момент истины»**: В начале игры происходит автоматический бросок кубика для определения очередности ходов.
 * **Интерактивные элементы**:
   * 🐍 **Змеи**: Отбрасывают назад на 6 клеток.
   * 🐉 **Длинные змеи**: Отбрасывают назад на 12 клеток.
   * ⬆️ **Лестницы**: Продвигают вперед на 6 клеток.
   * 🪜 **Длинные лестницы**: Продвигают вперед на 12 клеток.
* **Режимы игры (Сложность)**: Выберите целевое количество очков перед началом:
   * **Легкий**: 50 очков
   * **Нормальный**: 75 очков
   * **Сложный**: 100 очков
Если выпавшее число превышает лимит, игрок остается на месте.
### 🚀 Как запустить
 1. Убедитесь, что у вас установлен Python 3.10 или выше.
 2. Скачайте файл Snakes and Stairs.py.
 3. Запустите его через терминал:
   python "Snakes and Stairs.py
### 🛠 Управление
 * Введите количество игроков (2, 3 или 4).
 * Введите имена. Чтобы добавить бота, оставьте поле имени пустым.
 * В процессе игры нажимайте **Enter**, чтобы бросить кубик за своего персонажа. Бот «бросает» кубик автоматически.
## 📝 Описание второго коммита (Commit Message)
**Заголовок:** feat: добавлен выбор состава игроков и механика "Момент истины"
**Описание:**
 * **Мультиплеер:** Добавлена возможность выбора количества игроков (от 2 до 4). Реализована поддержка ботов (COMPUTER1-3), если поле имени остается пустым.
 * **Момент истины:** Добавлен алгоритм определения очередности ходов в начале игры. Система бросает кубики за каждого участника и сортирует их по убыванию (исключая дубликаты путем переброса).
 * **Логика передвижения:** Добавлены классы Human и Computer. Реализована функция brosok с обработкой специальных полей (змеи, лестницы, перелет за финишную черту).
 * **Финальный рейтинг:** Реализована система распределения мест (Победитель, Призер, Проигравший) в зависимости от количества участников.
 * 
