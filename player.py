def place_player(game_map):
    player_x, player_y = 1, 1  #Это позиция по умолчнанию
    game_map[player_y][player_x] = 'P' #А это ты... Да-да ты! ИГРОК!
    return player_x, player_y

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
        game_map[player_y][player_x] = ' '
        game_map[new_y][new_x] = 'P'
        return new_x, new_y

    return player_x, player_y

def init_player():
    return {
        "HP": 20,
        "MP/SP": 10,
        "ARM": 5,
        "DMG": 3,
        "inventory": []
    }

def display_player_stats(player):
    print(f"HP: {player['HP']} | MP/SP: {player['MP/SP']} | ARM: {player['ARM']} | DMG: {player['DMG']}")

def display_inventory(player):
    print("\n=== Инвентарь ===")
    if player["inventory"]:
        for item in player["inventory"]:
            print(f"- {item}")
    else:
        print("Инвентарь пуст.")
    print("=================\n")

def interact(player, game_map, player_x, player_y):
    print("\nВыберите действие:")
    print("1 - Поднять предмет")
    print("2 - Атаковать врага")

    exit_marker = None
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = player_x + dx
        ny = player_y + dy
        if 0 <= nx < len(game_map[0]) and 0 <= ny < len(game_map):
            cell = game_map[ny][nx]
            if cell in ['[]', 'D', '^', '<', 'v']:
                exit_marker = cell
                break

    if exit_marker:
        print("3 - Перейти на новую локацию")

    action = input("Введите номер действия: ")

    if action == '1':  #Поднятие предмета + проверка на нахождения предмета поблизости
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = player_x + dx
            ny = player_y + dy
            if 0 <= nx < len(game_map[0]) and 0 <= ny < len(game_map):
                if game_map[ny][nx] == '*':
                    print("Вы подобрали предмет!")
                    player["inventory"].append("Палка")
                    game_map[ny][nx] = ' '
                    return None
            
            #Поднятие СПЕЦИАЛЬНОГО предмета (для конца игры)
            if 0 <= nx < len(game_map[0]) and 0 <= ny < len(game_map):
                if game_map[ny][nx] == '*!':                 
                    #Финальное сообщение
                    print("\n" * 999)  #Очищаем экран
                    print('"Любопытство кошку сгубило", как говорится. \nРешив прогуляться по степи, вы наткнулись на "странное" растение и решили сорвать его, но это было фатальной ошибкой. \nВолшебные корни растения, державшую могучую землю, потеряли возможность и не смогли удержать вас и то, что было рядом. \nВы провалились, больше о вас никто не слышал... Или нет?')
                    input("\nПродолжение (не)следует. Нажмите Enter для выхода...")
                    exit()
                        
        print("Рядом нет предметов для поднятия.")

    elif action == '2':  #Процесс атаки
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = player_x + dx
            ny = player_y + dy
            if 0 <= nx < len(game_map[0]) and 0 <= ny < len(game_map):
                if game_map[ny][nx] == 'X':
                    print("Вы атаковали врага! Враг побежден.")
                    game_map[ny][nx] = ' '
                    return None
        print("Здесь нет врагов для атаки.")

    elif action == '3' and exit_marker: #Метки выхода из локаций
        print("\nВы покидаете текущую зону...")
        
        if exit_marker == '[]':
            print("\nОбучение завершено!")
            return "village"
       
        elif exit_marker == 'D':
            return "village"
        
        elif exit_marker == '^':
            return "forest"
        
        elif exit_marker == '<':
            return "lake"
        
        elif exit_marker == 'v':
            return "steppe"

    else:
        print("Некорректный выбор.")

    return None