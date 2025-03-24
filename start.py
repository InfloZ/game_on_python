from tutorial import tutorial, get_tutorial_enemies
from map import print_map, create_map
from player import place_player, move_player, init_player, display_player_stats, display_inventory, interact
from village import create_village_map, get_village_enemies
from forest import create_forest_map, get_forest_enemies
from lake import create_lake_map, get_lake_enemies
from steppe import create_steppe_map, get_steppe_enemies

def main():
    choice = input('Хотите пройти обучение? (y/n). Для запуска свободного (пользовательского) режима - (f): ').lower()

    if choice == 'n':
        confirm = input("Ты уверен, что хочешь пропустить обучение? (y/n): ").lower()
        if confirm == 'n':
            choice = 'y'  

    elif choice == 'f':
        size = int(input("Введите размер карты (от 25 до 50): "))
        game_map, enemies = create_map(size)
        player_x, player_y = place_player(game_map)
        player = init_player()
        
        #В случае отказа от обучения запускается классический свободный режим
        while True:
            print_map(game_map)
            display_player_stats(player)
            move = input("Введите направление (WASD - передвижение, I - инвентарь, L - дебагер, Q - выход): ").lower()
                    
            if move == 'q': #Это выход (отличная кнопка для тех, кто не знает как играть)
                break
            elif move == 'i': #Вызов инвентаря
                display_inventory(player)
            elif move == 'l':  #Вызов дебагера
                debugger(player, player_x, player_y, game_map, enemies)
            elif move == 'z':  #Взаимодействие с объектами
                next_location = interact(player, game_map, player_x, player_y)
            else:
                player_x, player_y = move_player(game_map, player_x, player_y, move)

    if choice == 'y':
        game_map = tutorial()
        current_location = "tutorial"
        enemies = get_tutorial_enemies(game_map)
    
    else:
        print("\nВы начинаете игру в Деревне.")
        print("Легенда: H - хижина | [o] - колодец | C - сарай | ^ - выход в лес | < - выход на озеро | v - выход в степь")
        game_map = create_village_map()
        current_location = "village"
        enemies = get_village_enemies(game_map)

    player_x, player_y = place_player(game_map)
    player = init_player()

    while True:
        print_map(game_map)
        display_player_stats(player)
        move = input("Введите направление (WASD - передвижение, I - инвентарь, L - дебагер, Q - выход): ").lower()

        if move == 'q': #Это выход (отчличная кнопка для тех, кто не знает как играть)
            break
        
        elif move == 'i': #Вызов инвентаря
            display_inventory(player)
        
        elif move == 'l':  #Вызов дебаггера
            debugger(player, player_x, player_y, game_map, enemies)
        
        elif move == 'z':  #Взаимодействие с объектами
            next_location = interact(player, game_map, player_x, player_y)

            if next_location:
                if next_location == "village":
                    print("\n" * 80) #Очищаем экран
                    
                    print("\nВы попадаете в Деревню.")
                    print("Легенда: H - хижина | [o] - колодец | C - сарай | ^ - выход в лес | < - выход на озеро | v - выход в степь")
                    game_map = create_village_map()
                    current_location = "village"
                    enemies = get_village_enemies(game_map)
                
                elif next_location == "forest":
                    print("\nПереход в Лес...")
                    print("Легенда: Q - пещера | O - нора | T - деревья | D - выход в деревню")
                    game_map = create_forest_map()
                    current_location = "forest"
                    enemies = get_forest_enemies(game_map)
                
                elif next_location == "lake":
                    print("\nПереход к Озеру...")
                    print("Легенда: W - вода | F - хижина рыбака | Δ - палатка | D - выход в деревню")
                    game_map = create_lake_map()
                    current_location = "lake"
                    enemies = get_lake_enemies(game_map)
                
                elif next_location == "steppe":
                    print("\nПереход в Степь...")
                    print("Легенда: L - могила | W - лужа | T - деревья | D - выход в деревню")
                    game_map = create_steppe_map()
                    current_location = "steppe"
                    enemies = get_steppe_enemies(game_map)

                #При смене локации обновляем координаты игрока (чтобы игрок не исчез с локации)
                player_x, player_y = place_player(game_map)
                continue

        else:
            player_x, player_y = move_player(game_map, player_x, player_y, move)

def debugger(player, player_x, player_y, game_map, enemies):
    print("\n===Дебаггер===")
    print(f"Координаты игрока: ({player_x}, {player_y})")
    display_player_stats(player)
    
    print("\nТекущие враги на карте:")
    if enemies:
        for enemy in enemies:
            print(f"Враг на координатах: {enemy}")
    else:
        print("Нет врагов на карте.")

    print("\nКарта:")
    print_map(game_map)
    print("===Дебаггер===\n")

if __name__ == "__main__":
    main()