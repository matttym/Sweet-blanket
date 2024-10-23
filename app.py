# Размеры игрового поля
rows = 4
cols = 5

# Игровое поле
board = [['.' for _ in range(cols)] for _ in range(rows)]

# Символы игроков
players = ['X', 'O', 'H']

# Подсчет штрафных очков для каждого игрока
fine = {player: 0 for player in players}


# Отображение игрового поля
def print_board():
    for row in board:
        print(' '.join(row))
    print()


# Проверка и начисление штрафных очков
def check_penalties(x, y, player):
    penalty = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == player:
            penalty += 1

    return penalty


# Основной игровой цикл
def play_game():
    move_count = 0
    total_moves = rows * cols

    while move_count < total_moves:
        player = players[move_count % 3]

        print(f"Ход игрока {player}. Введите координаты (x y):")
        try:
            x, y = map(int, input().split())

            # Проверка корректности ввода
            if not (1 <= x <= rows and 1 <= y <= cols):
                print("Некорректные координаты. Попробуйте снова.")
                continue
            if board[x-1][y-1] != '.':
                print("Клетка уже занята. Попробуйте снова.")
                continue

            # Обновляем поле и считаем штрафные очки
            board[x-1][y-1] = player
            penalty = check_penalties(x-1, y-1, player)
            fine[player] += penalty

            # Отображаем игровое поле
            print_board()

            # Увеличиваем счетчик ходов
            move_count += 1

        except ValueError:
            print("Некорректный ввод. Введите два числа через пробел.")

    # Определение победителя
    print("Игра окончена!")
    print("Штрафные очки:")
    for player, penalty in fine.items():
        print(f"Игрок {player}: {penalty}")

    # Находим победителя с наименьшим количеством штрафных очков
    winner = min(fine, key=fine.get)
    print(f"Победитель: игрок {winner}!")


# Начало игры
print("Игра «Лоскутное одеяло» началась!")
print_board()
play_game()
