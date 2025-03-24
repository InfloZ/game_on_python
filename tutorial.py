def create_tutorial_map():
    size = 10
    game_map = [[' ' for _ in range(size)] for _ in range(size)]
    
    #Границы стен
    for i in range(size):
        game_map[0][i] = '#'
        game_map[size - 1][i] = '#'
        game_map[i][0] = '#'
        game_map[i][size - 1] = '#'
    
    #Метки
    game_map[1][1] = 'P' #Игрок
    game_map[3][3] = '*' #Предмет
    game_map[5][5] = 'X' #Враг
    game_map[8][8] = '[]' #Выход

    return game_map

def tutorial():
    print("\nДобро пожаловать в обучение!")
    input("Нажмите Enter для продолжения...")

    print("\nКлавиши WASD позволяют вашему герою передвигаться.")
    input("Нажмите Enter для продолжения...")

    print("\nW - вверх, S - вниз, A - влево, D - вправо.")
    print("Если ты увидишь что-нибудь на своём пути, то ты можешь с ним повзаимодействовать нажав на клавишу Z и выбрав действие.")
    input("Нажмите Enter для продолжения...")

    print("\nХм... Думаю, тебе стоит показать карту!")
    input("Нажмите Enter для продолжения...")

    print("\n" * 80) #Очищаем экран

    print("\nСМОТРИ! Подойди к новому объекту (*) и подбери его (клавиша Z и действие). Подобранные вещи можно увидеть в инвентаре (нажмите I).")
    print("\nТОЛЬКО ОСТОРОЖНО! Похоже, это существо (X) не очень дружелюбно!")
    print('\nЕсли ты хочешь подраться с ним, то нажми Z, чтобы выбрать действие, затем выбери "Атаковать"!\n')

    return create_tutorial_map()

#Это для подсчёта врагов (дебага)
def get_tutorial_enemies(game_map):
    enemies = []
    for y, row in enumerate(game_map):
        for x, cell in enumerate(row):
            if cell == 'X':
                enemies.append((x, y))
    return enemies