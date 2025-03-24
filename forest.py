def create_forest_map():
    size = 10
    game_map = [[' ' for _ in range(size)] for _ in range(size)]

    #Границы карты
    for i in range(size):
        game_map[0][i] = '#'
        game_map[size - 1][i] = '#'
        game_map[i][0] = '#'
        game_map[i][size - 1] = '#'

    #Деревья
    game_map[3][3] = 'T'
    game_map[4][4] = 'T'
    game_map[5][3] = 'T'

    #Нора
    game_map[8][8] = 'O'
    game_map[1][8] = 'O'

    #Пещера
    game_map[7][1] = 'Q'
    game_map[7][2] = 'Q'
    game_map[8][1] = 'Q'
    game_map[8][2] = 'Q'

    #Выход обратно в деревню
    game_map[size - 1][size // 2] = 'D'

    return game_map

#Это для подсчёта врагов (дебага)
def get_forest_enemies(game_map):
    enemies = []
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == 'X':
                enemies.append((x, y))
    return enemies