#Ставим игрока на стандартную позицию 
def place_player(game_map):
    player_x, player_y = 1, 1
    game_map[player_y][player_x] = 'P'
    return player_x, player_y

#Перемещаем игрока, если нет стены или врага
def move_player(game_map, player_x, player_y, direction):
    new_x, new_y = player_x, player_y

    if direction == 'w':
        new_y -= 1
    elif direction == 's':
        new_y += 1
    elif direction == 'a':
        new_x -= 1
    elif direction == 'd':
        new_x += 1

    if game_map[new_y][new_x] == ' ':
        game_map[player_y][player_x] = ' '  #Очистка старой позиции
        game_map[new_y][new_x] = 'P'  #Перемещение игрока
        return new_x, new_y

    return player_x, player_y  #Если стена или враг, остаемся на месте

#Характеристики игрока
def init_player():
    return {
        "HP": 20, #Жизни
        "MP/SP": 10, #Мана
        "ARM": 5, #Защита
        "DMG": 3, #Урон
        "inventory": []  #Инвентарь
    }

#Вывод характеристик игрока
def display_player_stats(player):
    print(f"HP: {player['HP']} | MP/SP: {player['MP/SP']} | ARM: {player['ARM']} | DMG: {player['DMG']}")

#Вывод содержимого инвентаря
def display_inventory(player):
    print("\n=== Инвентарь ===")
    if player["inventory"]:
        for item in player["inventory"]:
            print(f"- {item}")
    else:
        print("Инвентарь пуст.")
    print("=================\n")