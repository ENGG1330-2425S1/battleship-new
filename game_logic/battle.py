import random
import time
from game_logic.helper import (
    check_positions_attacked,
    check_positions_within_bounds,
    create_position_array,
    generate_cross_positions,
    generate_horizontal_positions,
    generate_vertical_positions,
    get_all_attacked_positions,
    handle_position_input,
)
from matrix import index_to_position, position_to_index


def add_players():
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


def select_attack_method():
    print("Select your attack method:")
    print("h - Horizontal bomb")
    print("v - Vertical bomb")
    print("c - Cross bomb")
    print("b - Common bomb")  # New option for common bomb
    while True:
        choice = input("Enter your choice (h, v, c, b): ").strip().lower()
        if choice in ["h", "v", "c", "b"]:
            return choice
        print("Invalid choice. Please try again.")


def attack(row, col, matrix, hitted_matrix, attack_type):
    """
    Executes an attack on the game board based on the specified attack type.
    Parameters:
    row (int): The row index of the attack.
    col (int): The column index of the attack.
    matrix (list of list of str): The game board matrix representing the current state of the game.
    hitted_matrix (list of list of str): The matrix representing the positions that have been hit.
    attack_type (str): The type of attack to be performed. Can be "h" for horizontal, "v" for vertical,
                       "c" for cross, or "b" for a common bomb (single position).
    Returns:
    tuple: A tuple containing:
        - hitted_matrix (list of list of str): The updated matrix representing the positions that have been hit.
        - bool: A boolean indicating whether the attack was successful.
        - str: A message indicating the result of the attack.
    """
    # Get the list of position to be attacked based on the attack type
    if attack_type == "h":
        positions = generate_horizontal_positions(row, col)
    elif attack_type == "v":
        positions = generate_vertical_positions(row, col)
    elif attack_type == "c":
        positions = generate_cross_positions(row, col)
    elif attack_type == "b":  # For common bomb
        positions = [(row, col)]  # Only attack the specified position

    # Check if all positions are within bounds
    if not check_positions_within_bounds(matrix, positions):
        return (
            hitted_matrix,
            False,
            "One or more positions are out of bounds. Try again.",
        )

    # Check if all positions are valid
    if check_positions_attacked(hitted_matrix, positions):
        return (
            hitted_matrix,
            False,
            "One or more positions have already been attacked. Try again.",
        )

    # Process the attacks for all positions
    hit_positions = []
    for pos in positions:
        r, c = pos
        if matrix[r][c] != "~":
            hitted_matrix[r][c] = "X"
            label = index_to_position([r, c])
            hit_positions.append(label)
        else:
            hitted_matrix[r][c] = "O"

    if len(hit_positions) > 1:
        return hitted_matrix, True, f"hit at positions: {', '.join(hit_positions)}"
    elif len(hit_positions) == 1:
        return hitted_matrix, True, f"hit at position: {hit_positions[0]}"
    else:
        return hitted_matrix, True, "missed"


def user_attack_prompt(matrix):
    # Get attack position from user
    position = input("Enter your attack position (e.g. A1): ")

    [row, col], error_message = handle_position_input(position, matrix)

    if error_message:
        return [row, col], None, error_message

    # Select the attack method
    attack_type = select_attack_method()

    return [row, col], attack_type, error_message


def random_attack(player_grid, player_hitted_grid):
    attack_methods = ["h", "v", "c", "b"]  # Available attack methods
    while True:
        # Find the positions that have not been attacked
        position_array = create_position_array(player_grid)
        attacked_array = get_all_attacked_positions(player_hitted_grid)
        valid_positions = list(set(position_array) - set(attacked_array))

        while True:
            position_to_attack = random.choice(
                valid_positions
            )  # Randomly select a position
            row, col = position_to_index(
                position_to_attack
            )  # Convert position to row and column
            attack_type = random.choice(attack_methods)  # Randomly select attack method

            # Perform the attack
            player_hitted_grid, is_valid_attack, message = attack(
                row, col, player_grid, player_hitted_grid, attack_type
            )

            if is_valid_attack:
                attack_names = {
                    "h": "Horizontal bomb",
                    "v": "Vertical bomb",
                    "c": "Cross bomb",
                    "b": "Single bomb",
                }
                message = (
                    f"Computer uses {attack_names[attack_type]}!\nComputer {message}"
                )
                return player_hitted_grid, message


def merge_grids(hitted_matrix, matrix2):
    """
    Merges two grids by replacing the '~' characters in the hitted_matrix with the corresponding values from matrix2.

    Args:
        hitted_matrix (list of list of str): The first grid, where '~' represents a placeholder to be replaced.
        matrix2 (list of list of str): The second grid, providing replacement values for '~' in the hitted_matrix.

    Returns:
        list of list of str: A new grid where '~' in hitted_matrix is replaced by the corresponding values from matrix2.
    """
    return [
        [
            (
                hitted_matrix[row][col]
                if hitted_matrix[row][col] != "~"
                else matrix2[row][col]
            )
            for col in range(len(hitted_matrix[row]))
        ]
        for row in range(len(hitted_matrix))
    ]


def check_win(matrix):
    """
    Check if the game has been won by counting the number of hits.

    Args:
        matrix (list of list of str): A 2D list representing the game board,
                                      where each cell contains either a hit ("X") or other values.

    Returns:
        bool: True if the number of hits ("X") equals the target count (17), indicating a win.
              False otherwise.
    """
    target_count = 17
    count = sum(cell == "X" for row in matrix for cell in row)
    return count == target_count  # Return True if count matches target_count
