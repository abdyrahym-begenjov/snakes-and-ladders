# snakes-and-ladders
Snakes and Ladders
# 🐍 Snakes and Ladders (Змеи и Лестницы) 🪜
## English
An interactive, multi-language, console-based digital adaptation of the classic "Snakes and Ladders" board game, built entirely in Python. Play with up to 4 players, including local human players and computer opponents. This version modernizes the timeless classic by introducing unique inventory systems, tactical abilities, variable game difficulties, and a persistent leaderboard system.
### ✨ Key Features
 * **Dynamic Difficulties:** Tailor your match length and board intensity with three distinct difficulties (Easy with a 50-step goal, Normal with a 75-step goal, or Hard with a grueling 100-step goal).
 * **Tactical Power-ups:** Go beyond pure dice luck! Human players can invoke specialized match abilities:
   * *Teleportation:* Swap positions with an opponent to steal their momentum.
   * *Double Dice:* Multiply your next roll by 2 for a major speed boost.
   * *Rocket:* Propel yourself safely forward by exactly 10 squares.
   * *Ice:* Freeze an opposing player, forcing them to skip their next active turn.
 * **Persistent Highscores:** Real-time data storage ensures your total point accumulation across all matches is saved locally via JSON architecture.
 * **Purist Multipliers:** Finish a game without spending a single active ability item to earn double experience points at the victory screen.
 * **Multi-language Support:** Native dynamic translation capabilities supporting English (en) and Russian (ru).
### 🚀 Getting Started
#### Prerequisites
Make sure you have Python 3.10 or higher installed, as this game utilizes modern pythonic structures like match-case statements.
#### Setup & Execution
 1. Ensure all dependent helper modules (translator.py, players.py, utils.py, propython.py, brosok.py) and data structures (data.json, base.json) are located in the exact same directory as your main file.
 2. Launch the terminal and navigate to your project directory.
 3. Run the primary entry point file using the command: python "Snakes and Stairs.py"
### 🎮 Game Rules & Loop
 1. **Setup:** Choose your desired language setting on your first launch. Select **Game** from the primary home terminal selection menu.
 2. **Player Configuration:** Input the total count of active competitors (2 to 4 players). Type your name to fill a slot; leaving the prompt completely blank automatically configures an computer player to step into the match.
 3. **The Roll of Destiny:** A pre-game dice simulation evaluates everyone's starting agility. The highest rolling sequence dictates the official active turn order.
 4. **Gameplay Options:** On your active turn, simply press Enter to trigger a normal random dice roll (1-6). Alternatively, text-invoke special ability perks like double, teleport, rocket, or ice to turn the tide.
 5. **Hazards & Aids:** * Stepping onto a basic Snake (🐍) or a Large Snake (🐍🐍) drags you down. Beware of the catastrophic *Dangerous Snake* on Hard mode!
   * Stepping onto Ladders (🪜) or Large Ladders (🪜🪜) accelerates your climb toward the goal.
 6. **Victory Condition:** Navigate precisely to the finish line parameter. Landing over the finish line bounces your placement backward. Matches conclude with full placement distributions, crowning an ultimate winner and acknowledging runners-up!
     
## Русский
Интерактивная многоязычная консольная адаптация классической настольной игры «Змеи и лестницы», написанная на Python. Играйте в компании до 4 человек, комбинируя реальных игроков и компьютерных соперников. Эта версия превращает чистую случайность в тактическое противостояние благодаря системе суперспособностей, разным уровням сложности и сохранению рекордов.
### ✨ Основные возможности
 * **Динамическая сложность:** Настраивайте длину матча под себя. Доступны три режима: Легкий (цель — 50 шагов), Нормальный (75 шагов) и Сложный (100 шагов с опасными ловушками).
 * **Тактические способности:** Влияйте на исход матча с помощью уникального инвентаря (доступно для игроков-людей):
   * *Телепортация (teleport):* Поменяйтесь местами с любым соперником на доске.
   * *Удвоение (double):* Умножьте результат следующего броска на 2.
   * *Ракета (rocket):* Безопасно переместитесь вперед ровно на 10 клеток.
   * *Заморозка (ice):* Заставьте выбранного противника полностью пропустить следующий ход.
 * **Таблица рекордов:** Все набранные очки за победы автоматически сохраняются в локальной базе данных JSON, формируя глобальный лидерборд.
 * **Множитель для хардкорщиков:** Доберитесь до финиша, не потратив ни одной способности, чтобы получить заслуженное удвоение очков в таблицу рекордов.
 * **Полная локализация:** Встроенная поддержка двух языков с возможностью переключения — Английский (en) и Русский (ru).
### 🚀 Запуск игры
#### Требования к системе
Для корректной работы игры требуется установленный интерпретатор Python версии 3.10 или выше (в коде используются конструкции ветвления match-case).
#### Настройка и запуск
 1. Убедитесь, что все вспомогательные модули (translator.py, players.py, utils.py, propython.py, brosok.py) и файлы данных (data.json, base.json) находятся в одной папке с основным файлом скрипта.
 2. Откройте терминал/командную строку и перейдите в папку проекта.
 3. Запустите игру с помощью команды: python "Snakes and Stairs.py"
### 🎮 Правила и игровой процесс
 1. **Подготовка:** При первом запуске выберите предпочитаемый язык. В главном текстовом меню введите **Game** (или **Игра** при выбранном русском интерфейсе).
 2. **Настройка лобби:** Укажите количество участников (от 2 до 4). Введите имена для реальных игроков. Если оставить поле ввода имени пустым, система автоматически создаст компьютерного бота.
 3. **Определение очередности:** Игра автоматически бросает кубик для каждого участника. Тот, у кого выпало наибольшее число, получает право ходить первым.
 4. **Ваш ход:** В свой ход просто нажмите Enter, чтобы совершить стандартный бросок кубика (от 1 до 6). Чтобы активировать способность, введите в консоль текстовую команду: double, teleport, rocket или ice.
 5. **Препятствия и бонусы:**
   * Попадание на клетку со Змеей (🐍 или 🐍🐍) сбрасывает вас назад. Опасайтесь *Dangerous Snake* на сложном режиме!
   * Попадание на Лестницу (🪜 или 🪜🪜) мгновенно поднимает вас ближе к финишу.
 6. **Условие победы:** Чтобы победить, необходимо остановиться строго на финальной клетке. Если выпавшее число превышает финишную отметку, персонаж отскакивает назад. Игра продолжается до распределения всех призовых и аутсайдерских мест.
