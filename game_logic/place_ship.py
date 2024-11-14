import random
from cli import clear_console, matrix_output_preprocess
from game_logic.helper import (
    create_position_array,
    dict_find_key_by_value,
    handle_position_input,
    validate_direction_input,
)
from constants import ships, ship_labels


def handle_place_ships(matrix, ship_name, direction, row, col):
    """
    Places a ship on the game board matrix.

    Args:
        matrix (list of list of str): The game board matrix.
        ship_name (str): The name of the ship to be placed.
        direction (str): The direction of the ship placement ('H' for horizontal, 'V' for vertical).
        row (int): The starting row index for the ship placement.
        col (int): The starting column index for the ship placement.

    Returns:
        tuple: A tuple containing the updated matrix and a warning message (if any).
            The warning message will be None if the ship is placed successfully.
            Possible warning messages include:
            - "Warning! Ship placement is out of horizontal bounds."
            - "Warning! Position already occupied by {existing_ship_name}."
            - "Warning! Ship placement is out of vertical bounds."
            - "Warning! Invalid direction."
    """
    ship_length = ships[ship_name]
    if direction == "H":
        if col + ship_length > len(matrix[0]):
            return matrix, "Warning! Ship placement is out of horizontal bounds."
        for i in range(ship_length):
            if matrix[row][col + i] != "~":
                existing_ship = matrix[row][col + i]
                existing_ship_name = dict_find_key_by_value(ship_labels, existing_ship)
                return (
                    matrix,
                    f"Warning! Position already occupied by {existing_ship_name}.",
                )
        for i in range(ship_length):
            matrix[row][col + i] = ship_labels[ship_name]
    elif direction == "V":
        if row + ship_length > len(matrix):
            return matrix, "Warning! Ship placement is out of vertical bounds."
        for i in range(ship_length):
            if matrix[row + i][col] != "~":
                existing_ship = matrix[row + i][col]
                existing_ship_name = dict_find_key_by_value(ship_labels, existing_ship)
                return (
                    matrix,
                    f"Warning! Position already occupied by {existing_ship_name}.",
                )
        for i in range(ship_length):
            matrix[row + i][col] = ship_labels[ship_name]
    else:
        return matrix, "Warning! Invalid direction."
    return matrix, None


def user_place_ships(matrix):
    """
    Allows the user to place ships on the game board.

    Args:
        matrix (list of list of str): The game board matrix where ships will be placed.

    Returns:
        list of list of str: The updated game board matrix with ships placed.

    The function prompts the user to place each ship by specifying its direction
    (horizontal or vertical) and its starting position on the board. It validates
    the user's input and updates the game board accordingly. If there are any errors
    in the input, it displays an error message and prompts the user to try again.
    """
    error_message = None
    for ship_name in ships.keys():
        placed = False
        while not placed:
            clear_console()
            print("General, place your ships!")
            print("-" * 40)
            print(matrix_output_preprocess(matrix))
            print("-" * 40)
            if error_message is not None:
                print(error_message)
                error_message = None
            print(f"Placing {ship_name}...")

            direction = input("Enter direction (H or V): ")
            result, error_message = validate_direction_input(direction)
            if not result:
                continue

            position = input("Enter the position of the ship. (e.g. A1): ")
            [row, col], error_message = handle_position_input(position, matrix)
            if [row, col] is None:
                continue

            matrix, error_message = handle_place_ships(
                matrix, ship_name, direction, row, col
            )
            if matrix[row][col] == ship_labels[ship_name]:
                placed = True
    return matrix


def random_place_ship(matrix):
    """
    Randomly places ships on the given game board matrix.

    Args:
        matrix (list of list of str): The game board matrix where ships will be placed.

    Returns:
        list of list of str: The updated game board matrix with ships placed.

    The function iterates over all ships defined in the `ships` dictionary and attempts to place each ship
    randomly on the board. It chooses a random direction (horizontal or vertical) and a random position
    on the board. It then calls helper functions to handle the placement and checks if the ship was 
    successfully placed. If not, it retries until the ship is placed correctly.
    """
    for ship_name in ships.keys():
        placed = False
        while not placed:
            direction = random.choice(["H", "V"])
            position = random.choice(create_position_array(matrix))
            [row, col], _ = handle_position_input(position, matrix)

            matrix, _ = handle_place_ships(matrix, ship_name, direction, row, col)

            if matrix[row][col] == ship_labels[ship_name]:
                placed = True

    return matrix
