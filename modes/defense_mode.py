from cli import clear_console, matrix_output_preprocess
from game_logic.battle import check_win, merge_grids, random_attack, add_players
from game_logic.helper import display_rankings, setup_grid
from game_logic.place_ship import user_place_ships


def defensemode(player_name):
    # Set up the ocean grid for the player
    player_grid = setup_grid()
    player_hitted_grid = setup_grid()

    player_grid = user_place_ships(player_grid)
    clear_console()

    counter = 1

    # Game loop
    while True:
        clear_console()
        print(f"Round {counter}")
        print("-" * 30)

        print(matrix_output_preprocess(merge_grids(player_hitted_grid, player_grid)))
        print("-" * 30)
        input("Press Enter to continue...")

        player_hitted_grid, message = random_attack(player_grid, player_hitted_grid)
        clear_console()

        print(message)
        print("-" * 30)
        print(matrix_output_preprocess(merge_grids(player_hitted_grid, player_grid)))
        print("-" * 30)
        input("Press Enter to continue...")

        if "hit" in message:
            if check_win(merge_grids(player_hitted_grid, player_grid)):
                break
            continue
        else:
            break

    # Final result display
    clear_console()
    print(f"Computer won in round {counter}!")
    print("-" * 30)
    print("Final Player Grid:")
    print(matrix_output_preprocess(player_hitted_grid))

    return counter  # Return the number of rounds taken


def run_defense_mode():
    """Main function to manage players and the game."""
    players = add_players()
    player_rounds = {}  # Dictionary to store each player's rounds

    for player in players:
        rounds = defensemode(player)  # Pass player name to defense mode
        player_rounds[player] = rounds

    # Display final rankings
    display_rankings(player_rounds)
