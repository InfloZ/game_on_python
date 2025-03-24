def create_village_map():
    size = 10
    game_map = [[' ' for _ in range(size)] for _ in range(size)]

    #Границы карты
    for i in range(size):
        game_map[0][i] = '#'
        game_map[size - 1][i] = '#'
        game_map[i][0] = '#'
        game_map[i][size - 1] = '#'

    #Хижины
    game_map[2][2] = 'H'
    game_map[2][5] = 'H'
    game_map[6][2] = 'H'
    game_map[7][3] = 'H'

    #Колодец
    game_map[4][2] = '[O]'

    #Сарай
    game_map[7][7] = 'C'
    game_map[7][8] = 'C'
    game_map[8][7] = 'C'
    game_map[8][8] = 'C'

    #Выходы:
    game_map[0][size // 2] = '^'   #Выход на север
    game_map[size // 2][0] = '<'     #Выход на запад
    game_map[size - 1][size // 2] = 'v'  #Выход на юг

    return game_map

#Это для подсчёта врагов (дебага)
def get_village_enemies(game_map):
    enemies = []
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == 'X':
                enemies.append((x, y))
    return enemies