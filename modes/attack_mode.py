from typing import List, Dict
from cli import clear_console, matrix_output_preprocess
from game_logic.battle import (
    add_players,
    attack,
    check_win,
    merge_grids,
    user_attack_prompt,
)
from game_logic.helper import display_rankings, setup_grid
from matrix import create_matrix, edit_all
from game_logic.place_ship import random_place_ship


def attackmode(player_name: str) -> int:
    """Play the attack mode for a specific player."""
    computer_grid = setup_grid()
    computer_hitted_grid = setup_grid()

    # Place ships on the grid
    computer_grid = random_place_ship(computer_grid)

    counter = 1
    message = None

    # Game loop
    while True:
        clear_console()
        if message:
            print(message)
            message = None
        # Display grids and round information
        print(f"{player_name}'s Turn")
        print(f"Round {counter}")
        print("-" * 30)
        print(matrix_output_preprocess(computer_hitted_grid))
        print("-" * 30)

        # Player's attack
        [row, col], attack_type, error_message = user_attack_prompt(computer_grid)

        if error_message:
            message = error_message
            continue

        computer_hitted_grid, is_valid_attack, message = attack(
            row, col, computer_grid, computer_hitted_grid, attack_type
        )

        if not is_valid_attack:
            continue

        # Check for win condition
        if check_win(merge_grids(computer_hitted_grid, computer_grid)):
            clear_console()
            print(f"You {message}")
            print(f"{player_name} won in round {counter}!")
            return counter  # Return the number of rounds taken

        # If the attack is a hit, continue to the next attack, not incrementing the round
        if message.startswith("h"):
            message = f"You {message}"
            continue
        else:
            message = f"You {message}"

        counter += 1  # Move to the next round


def run_attack_mode() -> None:
    """Main function to manage players and the game."""
    clear_console()

    players = add_players()
    player_rounds = {}  # Dictionary to store each player's rounds

    try:
        for player in players:
            rounds = attackmode(player)
            player_rounds[player] = rounds
            input("Enter to continue to the next player...")
    except KeyboardInterrupt:
        print("Game interrupted. Exiting...")

    display_rankings(player_rounds)


if __name__ == "__main__":
    run_attack_mode()
