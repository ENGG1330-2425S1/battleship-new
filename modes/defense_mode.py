from cli import clear_console, matrix_output_preprocess
from game_logic.battle import check_win, merge_grids, random_attack, add_players
from matrix import create_matrix, edit_all
from game_logic.place_ship import user_place_ships
from game_logic.welcome import welcome

def defensemode(player_name):
    # Set up the ocean grid for the player
    player_grid = edit_all(create_matrix(10), "~")
    player_hitted_grid = edit_all(create_matrix(10), "~")

    player_grid = user_place_ships(player_grid)
    clear_console()

    counter = 1
    computer_win = False

    # Game loop
    while True:
        print(f"Round {counter}")
        print("-" * 30)

        valid_attack = False  # Flag to track if the computer's attack is valid

        while not valid_attack:
            player_grid, player_hitted_grid, message = random_attack(player_grid, player_hitted_grid)

            # Process the result
            if message in ["hit", "miss"]:  # Ensure the message is valid
                valid_attack = True  # Valid attack, exit the loop
            else:
                print("Computer made an invalid attack. Retrying...")  # Notify about invalid attack

        # Display results
        print(matrix_output_preprocess(merge_grids(player_hitted_grid, player_grid)))
        print("-" * 30)
        print(f"Computer {message}")

        # Check if computer wins
        if check_win(merge_grids(player_hitted_grid, player_grid)):
            computer_win = True
            break

        # Increment counter for next round only if attack was valid
        counter += 1
        clear_console()

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
    print("\nRankings:")
    sorted_players = sorted(player_rounds.items(), key=lambda item: item[1])
    for rank, (name, rounds) in enumerate(sorted_players, start=1):
        print(f"No.{rank} {name} - {rounds} rounds")