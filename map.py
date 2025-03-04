#Создание карты (условие)
def create_map(size):
    if size < 4 or size > 15:
        print("Размер карты должен быть от 4 до 15. Установлен размер 6x6.")
        size = 6

    game_map = [[' ' for _ in range(size)] for _ in range(size)]

    #Создание границ стен
    for i in range(size):
        game_map[0][i] = '#'
        game_map[size - 1][i] = '#'
        game_map[i][0] = '#'
        game_map[i][size - 1] = '#'

    enemies = []

    #Размещение стен и врагов
    for row in range(2, size - 1, 2):  #Заполняем каждую вторую строку (2, 4, 6 и т.д.)
        for col in range(1, size - 1, 3):  #Каждые 3 столбца
            if (row + col) % 2 == 0:  #Чередуем стены и врагов
                game_map[row][col] = '#'
            else:
                game_map[row][col] = 'X'
                enemies.append((col, row))

    return game_map, enemies

#Печать карты на консоль
def print_map(game_map):
    for row in game_map:
        print(" ".join(row))
    print()
