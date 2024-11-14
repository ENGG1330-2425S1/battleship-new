from cli import clear_console, matrix_output_preprocess
from game_logic.battle import check_win, merge_grids, random_attack, user_attack
from matrix import create_matrix, edit_all
from game_logic.place_ship import user_place_ships, random_place_ship
from game_logic.welcome import welcome


def classic_mode():
    # Set up the ocean grid for both players
    player_grid = edit_all(create_matrix(10), "~")
    computer_grid = edit_all(create_matrix(10), "~")
    player_hitted_grid = edit_all(create_matrix(10), "~")
    computer_hitted_grid = edit_all(create_matrix(10), "~")

    # Place ships on the grid
    player_grid = user_place_ships(player_grid)
    computer_grid = random_place_ship(computer_grid)
    clear_console()

    counter = 1
    player_rounds_won = 0
    computer_rounds_lost = 0

    # Game loop
    while True:
        # Player's turn
        while True:
            print(matrix_output_preprocess(merge_grids(computer_hitted_grid, computer_grid)))
            print(matrix_output_preprocess(computer_grid))
            print(f"Player Round {counter}")
            print("-" * 30)
            print(matrix_output_preprocess(computer_hitted_grid))

            computer_grid, computer_hitted_grid, message = user_attack(computer_grid, computer_hitted_grid)
            clear_console()
            print(f"You {message}")

            # Check for hit
            if message[0] == "h":
                # Continue attacking if it's a hit
                continue
            else:
                # If it's a miss, break the loop
                break

        # Check if player won after their turn
        if check_win(merge_grids(computer_hitted_grid, computer_grid)):
            clear_console()
            print(f"You won in round {counter}!")
            player_rounds_won += 1
            print("-" * 30)
            print(matrix_output_preprocess(computer_hitted_grid))
            break

        clear_console()

        # Computer's turn
        while True:
            print(f"Computer Round {counter}")
            print("-" * 30)

            # Attempt to attack until a valid position is hit or missed
            while True:
                player_grid, player_hitted_grid, message = random_attack(player_grid, player_hitted_grid)

                # Check for hit
                if message[0] == "h":
                    print(matrix_output_preprocess(merge_grids(player_hitted_grid, player_grid)))
                    print(f"Computer Attack: {message}!")
                    continue  # Continue attacking if it's a hit
                else:
                    # If it's a miss, show the result and break the loop
                    print(matrix_output_preprocess(merge_grids(player_hitted_grid, player_grid)))
                    print("-" * 30)
                    print(f"Computer {message}")
                    input("Press Enter to continue...")
                    break  # Exit the attack loop on miss

            # Check if computer won after its turn
            if check_win(merge_grids(player_hitted_grid, player_grid)):
                clear_console()
                print(f"Computer won in round {counter}!")
                computer_rounds_lost += 1
                print("-" * 30)
                print(matrix_output_preprocess(player_hitted_grid))
                break

        # Increment counter for the next round
        counter += 1
        clear_console()

    # Print final ranking
    if player_rounds_won > 0:
        print(f"Winner! You won {player_rounds_won} round(s) against the computer.")
    else:
        print(f"Loser! You lost {computer_rounds_lost} round(s) against the computer.")


if __name__ == "__main__":
    classic_mode()