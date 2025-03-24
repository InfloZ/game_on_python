def create_steppe_map():
    size = 10
    game_map = [[' ' for _ in range(size)] for _ in range(size)]

    #Границы карты
    for i in range(size):
        game_map[0][i] = '#'
        game_map[size - 1][i] = '#'
        game_map[i][0] = '#'
        game_map[i][size - 1] = '#'

    #Палка
    game_map[4][4] = '*!'

    #Древние деревья
    game_map[6][4] = 'T'
    game_map[7][3] = 'T'
    game_map[8][5] = 'T'

    #Могила
    game_map[5][8] = 'L'
    game_map[7][8] = 'L'

    #Лужа
    game_map[1][7] = 'W'
    game_map[1][8] = 'W'
    game_map[2][7] = 'W'
    game_map[2][8] = 'W'

    #Выход обратно в деревню
    game_map[0][size // 2] = 'D'

    return game_map

#Это для подсчёта врагов (дебага)
def get_steppe_enemies(game_map):
    enemies = []
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == 'X':
                enemies.append((x, y))
    return enemies