def create_lake_map():
    size = 15
    game_map = [[' ' for _ in range(size)] for _ in range(size)]

    #Границы карты
    for i in range(size):
        game_map[0][i] = '#'
        game_map[size - 1][i] = '#'
        game_map[i][0] = '#'
        game_map[i][size - 1] = '#'
    
    #Враг
    game_map[11][2] = 'X'
    game_map[13][5] = 'X'

    #Озеро
    game_map[4][1] = 'W'
    game_map[4][2] = 'W'
    game_map[4][3] = 'W'
    game_map[4][4] = 'W'
    game_map[5][1] = 'W'
    game_map[5][2] = 'W'
    game_map[5][3] = 'W'
    game_map[5][4] = 'W'
    game_map[6][1] = 'W'
    game_map[6][2] = 'W'
    game_map[6][3] = 'W'
    game_map[6][4] = 'W'
    game_map[7][1] = 'W'
    game_map[7][2] = 'W'
    game_map[7][3] = 'W'
    game_map[7][4] = 'W'

    #Хижина рыбака
    game_map[12][11] = 'F'
    game_map[12][12] = 'F'
    game_map[13][11] = 'F'
    game_map[13][12] = 'F'

    #Палатка
    game_map[1][13] = 'Δ'
    game_map[3][12] = 'Δ'
    game_map[5][13] = 'Δ'

    #Вещь
    game_map[12][8] = '*'

    #Выход обратно в деревню
    game_map[size // 2][size - 1] = 'D'

    return game_map

#Это для подсчёта врагов (дебага)
def get_lake_enemies(game_map):
    enemies = []
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == 'X':
                enemies.append((x, y))
    return enemies