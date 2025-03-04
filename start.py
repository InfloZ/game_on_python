from map import create_map, print_map
from player import place_player, move_player, init_player, display_player_stats, display_inventory

#Вывод кнопок на интерфейс
def main():
    size = int(input("Введите размер карты (от 4 до 15): "))
    game_map, enemies = create_map(size)
    player_x, player_y = place_player(game_map)
    player = init_player()

    while True:
        print_map(game_map)
        display_player_stats(player)
        move = input("Введите направление (WASD - передвижение, I - инвентарь, L - дебагер, Q - выход): ").lower()
        
        if move == 'q': #Выход
            break
        elif move == 'i': #Вызов инвентаря
            display_inventory(player)
        elif move == 'l':  #Вызов дебагера
            debugger(player, player_x, player_y, game_map, enemies)
        else:
            player_x, player_y = move_player(game_map, player_x, player_y, move)

def debugger(player, player_x, player_y, game_map, enemies):
    print("\n===Дебагер===")
    print(f"Координаты игрока: ({player_x}, {player_y})")
    display_player_stats(player)
    
    print("\nТекущие враги на карте:")
    for enemy in enemies:
        print(f"Враг на координатах: {enemy}")
    
    print("\nКарта:")
    print_map(game_map)
    print("===Дебагер===")

if __name__ == "__main__":
    main()