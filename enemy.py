#Проверка на столкновение игрока с врагом
def check_for_enemy(player_x, player_y, game_map):
    if game_map[player_y][player_x] == 'X':
        game_map[player_y][player_x] = ' '  #Уничтожаем врага (ставим пустое место)
        print("Враг убит!")