#Псевдослучайный рандом (для размещения врагов например)
def pseudo_random(seed, max_value):
    a = 1234567
    c = 1013904223
    m = 2**32
    seed = (a * seed + c) % m
    return seed % max_value, seed

#Создание карты (условие)
def create_map(size):
    if size < 25 or size > 50:
        print("Размер карты должен быть от 25 до 50. Установлен размер 25x25.")
        size = 25  #Устанавливаем по умолчанию 25x25 если пользователь ввёл число не издиапазона

    game_map = [[' ' for _ in range(size)] for _ in range(size)]

    #Создание границ стен
    for i in range(size):
        game_map[0][i] = '#'
        game_map[size - 1][i] = '#'
        game_map[i][0] = '#'
        game_map[i][size - 1] = '#'

    enemies = []
    num_enemies = 12  #Количество врагов

    #Инициализация начального значения seed (это для рандома)
    seed = 12345

    #Размещение врагов
    for _ in range(num_enemies):
        x, seed = pseudo_random(seed, size - 2)  #Вычисляем x
        y, seed = pseudo_random(seed, size - 2)  #Вычисляем y

        #Чтобы враги не накладывались на стены
        while game_map[x + 1][y + 1] == 'X' or game_map[x + 1][y + 1] == '#':
            x, seed = pseudo_random(seed, size - 2)
            y, seed = pseudo_random(seed, size - 2)

        #Размещаем врага
        game_map[x + 1][y + 1] = 'X'  #Размещаем врага на клетке (x, y)
        enemies.append((y + 1, x + 1))  #Добавляем позицию врага в список

    return game_map, enemies

#Печать карты на консоль
def print_map(game_map):
    for row in game_map:
        print(" ".join(row))
    print()