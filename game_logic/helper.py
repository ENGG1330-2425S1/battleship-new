from matrix import row_label_to_index


def validate_direction_input(direction):
    """
    Validates the direction input for placing a ship in the Battleship game.

    Args:
        direction (str): The direction input, expected to be either "H" for horizontal or "V" for vertical.

    Returns:
        tuple: A tuple containing a boolean and a string. The boolean is True if the direction is valid,
               otherwise False. The string contains a warning message if the direction is invalid, otherwise None.
    """
    if direction != "H" and direction != "V":
        return False, "Warning! Invalid direction!"
    return True, None


def create_position_array(matrix):
    """
    Generates a list of position labels for a given 2D matrix.

    Args:
        matrix (list of list): A 2D list representing the matrix.

    Returns:
        list: A list of position labels in the format 'A1', 'A2', ..., 'B1', 'B2', etc.
    """
    position_array = []
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    for row in range(num_rows):
        row_label = chr(ord("A") + row)
        for col in range(num_cols):
            position = f"{row_label}{col + 1}"
            position_array.append(position)

    return position_array


def handle_position_input(position, matrix):
    """
    Handles the input of a position in a battleship game and converts it to matrix indices.

    Args:
        position (str): The position input by the user, expected in the format 'A1', 'B2', etc.
        matrix (list of list): The game board matrix to validate the position against.

    Returns:
        tuple: A tuple containing:
            - list: A list with two integers representing the row and column indices in the matrix if the input is valid.
            - str: An error message if the input is invalid, otherwise None.
    """
    if len(position) < 2:
        return None, "Invalid input! Please enter a valid position in the format 'A1'."

    row_part = position[0].upper()
    col_part = position[1:]

    if not row_part.isalpha() or not col_part.isdigit():
        return None, "Invalid input! Please enter a valid position in the format 'A1'."

    row = ord(row_part) - ord("A")
    col = int(col_part) - 1

    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return None, "Invalid input! Position is out of range."

    return [row, col], None


def dict_find_key_by_value(dictionary, value):
    """
    Find the first key in a dictionary that corresponds to a given value.

    Args:
        dictionary (dict): The dictionary to search through.
        value: The value to search for in the dictionary.

    Returns:
        The key associated with the given value if found, otherwise None.
    """
    for key, val in dictionary.items():
        if val == value:
            return key
    return None
