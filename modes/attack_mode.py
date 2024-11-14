from typing import List, Dict
from cli import clear_console, matrix_output_preprocess
from game_logic.battle import check_win, merge_grids, user_attack
from matrix import create_matrix, edit_all
from game_logic.place_ship import random_place_ship

GRID_SIZE = 10
WATER_SYMBOL = "~"


def add_players() -> List[str]:
    """Function to add player names."""
    players = []
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            if num_players < 1:
                raise ValueError("Number of players must be at least 1.")
            break
        except ValueError as e:
            print(e)

    for _ in range(num_players):
        name = input("Enter player name: ")
        players.append(name)
    return players


def setup_grid() -> List[List[str]]:
    """Create and initialize a grid with water symbols."""
    return edit_all(create_matrix(GRID_SIZE), WATER_SYMBOL)


def attackmode(player_name: str) -> int:
    """Play the attack mode for a specific player."""
    computer_grid = setup_grid()
    computer_hitted_grid = setup_grid()

    # Place ships on the grid
    computer_grid = random_place_ship(computer_grid)
    clear_console()

    counter = 1

    # Game loop
    while True:
        # Display grids and round information
        print(f"{player_name}'s Turn")
        print(f"Round {counter}")
        print("-" * 30)
        print(matrix_output_preprocess(computer_hitted_grid))

        # Player's attack
        computer_grid, computer_hitted_grid, message = user_attack(
            computer_grid, computer_hitted_grid
        )
        clear_console()
        print(f"You {message}")

        # Check for hit or miss based on the message content
        if "hit" in message.lower():
            continue  # If hit, continue to the next attack

        print("-" * 30)
        print(matrix_output_preprocess(computer_hitted_grid))
        print("-" * 30)

        # Check for win condition
        if check_win(merge_grids(computer_hitted_grid, computer_grid)):
            clear_console()
            print(f"{player_name} won in round {counter}!")
            return counter  # Return the number of rounds taken

        counter += 1  # Move to the next round
        clear_console()


def display_rankings(player_rounds: Dict[str, int]) -> None:
    """Display the final rankings of players based on the number of rounds taken."""
    print("\nRankings:")
    sorted_players = sorted(player_rounds.items(), key=lambda item: item[1])
    for rank, (name, rounds) in enumerate(sorted_players, start=1):
        print(f"No.{rank} {name} - {rounds} rounds")


def run_attack_mode() -> None:
    """Main function to manage players and the game."""
    clear_console()

    players = add_players()
    player_rounds = {}  # Dictionary to store each player's rounds

    try:
        for player in players:
            rounds = attackmode(player)
            player_rounds[player] = rounds
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")

    display_rankings(player_rounds)


if __name__ == "__main__":
    run_attack_mode()
