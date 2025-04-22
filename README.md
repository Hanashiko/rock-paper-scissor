# 🪨📄✂️ Rock-Paper-Scissors CLI Game

Це проста консольна реалізація гри **Камінь-Ножиці-Папір** на Python. Ви граєте проти комп’ютера, вводячи скорочені варіанти вибору, а гра рахує кількість перемог та загальну кількість ігор.

## 🚀 Швидкий старт

### Вимоги

- Python 3.7+

### Запуск

Склонуйте репозиторій та запустіть гру:

```bash
git clone https://github.com/Hanashiko/rock-paper-scissor.git
cd rock-paper-scissor
python main.py
```

## 🎮 Як грати

При запуску програма виведе інструкцію:

```
For playing, write:
'r' - rock,
'p' - paper,
's' - scissors
'st' for checking stats of games
'q' for quit the game
```

### Команди

- `r` — камінь  
- `p` — папір  
- `s` — ножиці  
- `st` — переглянути статистику  
- `q` — вийти з гри

### Приклад гри

```
Write your option: r
My choice - paper
I am win

Write your option: p
My choice - rock
You are winner!!!
```

## 📊 Статистика

У будь-який момент ви можете ввести `st`, щоб переглянути свою статистику:

```
We played - 5 times
You won 2 times
```

## 🧠 Логіка гри

- Камінь перемагає ножиці  
- Ножиці перемагають папір  
- Папір перемагає камінь  
- Однакові варіанти — нічия

## 📁 Структура коду

- `main()` — головний цикл гри  
- `isUserWin(user, computer)` — визначає результат раунду  
- `validation_user(choice)` — перевіряє введення користувача  
- Глобальні змінні `wins`, `tried` — для підрахунку статистики
