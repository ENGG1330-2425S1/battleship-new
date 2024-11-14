from cli import clear_console, matrix_output_preprocess
from game_logic.battle import (
    attack,
    check_win,
    merge_grids,
    random_attack,
    user_attack_prompt,
)
from game_logic.helper import setup_grid
from game_logic.place_ship import user_place_ships, random_place_ship


def run_classic_mode():
    # Set up the ocean grid for both players
    player_grid = setup_grid()
    computer_grid = setup_grid()
    player_hitted_grid = setup_grid()
    computer_hitted_grid = setup_grid()

    # Place ships on the grid
    player_grid = user_place_ships(player_grid)
    computer_grid = random_place_ship(computer_grid)
    clear_console()

    counter = 1
    player_win = False
    computer_win = False

    # Game loop
    while True:
        message = None

        # Player's turn
        while True:
            clear_console()
            if message:
                print(message)
                message = None

            print(f"Player Round {counter}")
            print("-" * 30)
            print(matrix_output_preprocess(computer_hitted_grid))
            print("-" * 30)

            [row, col], attack_type, error_message = user_attack_prompt(computer_grid)

            if error_message:
                message = error_message
                continue

            computer_hitted_grid, is_valid_attack, message = attack(
                row, col, computer_grid, computer_hitted_grid, attack_type
            )

            if not is_valid_attack:
                continue

            clear_console()
            print(f"You {message}")
            print("-" * 30)
            print(matrix_output_preprocess(computer_hitted_grid))
            print("-" * 30)
            input("Press Enter to continue...")

            # Check for win condition
            if check_win(merge_grids(computer_hitted_grid, computer_grid)):
                clear_console()
                print(f"Player won in round {counter}!")
                player_win = True
                break

            # If the attack is a hit
            if "hit" in message:
                continue

            message = None

            break  # Exit the player's turn loop

        if player_win:
            break  # Exit the game loop

        clear_console()

        # Computer's turn
        while True:
            print(f"Computer Round {counter}")
            print("-" * 30)
            print(
                matrix_output_preprocess(merge_grids(player_hitted_grid, player_grid))
            )
            print("-" * 30)
            input("Press Enter to continue...")

            player_hitted_grid, message = random_attack(player_grid, player_hitted_grid)

            clear_console()
            print(message)
            print("-" * 30)
            print(
                matrix_output_preprocess(merge_grids(player_hitted_grid, player_grid))
            )
            print("-" * 30)
            input("Press Enter to continue...")

            if "hit" in message:
                if check_win(merge_grids(player_hitted_grid, player_grid)):
                    clear_console()
                    print(f"Computer won in round {counter}!")
                    computer_win = True
                    break
                continue
            else:
                break

        if computer_win:
            break

        counter += 1


if __name__ == "__main__":
    run_classic_mode()
