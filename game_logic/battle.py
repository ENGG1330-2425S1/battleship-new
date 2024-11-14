import random
from game_logic.helper import handle_position_input
from matrix import index_to_row_label


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


def generate_horizontal_positions(start_row, start_col):
    return [(start_row, start_col + i) for i in range(5)]


def generate_vertical_positions(start_row, start_col):
    return [(start_row + i, start_col) for i in range(5)]


def generate_cross_positions(start_row, start_col):
    return [
        (start_row, start_col),  # Center
        (start_row - 1, start_col),  # Up
        (start_row + 1, start_col),  # Down
        (start_row, start_col - 1),  # Left
        (start_row, start_col + 1),  # Right
    ]


def user_attack(matrix, hitted_matrix):
    error_message = None
    message = None

    while True:
        # Display error message if any
        if error_message:
            print(error_message)
            error_message = None

        # Get attack position from user
        position = input("Enter your attack position (e.g. A1): ")
        [row, col], error_message = handle_position_input(position, matrix)

        if [row, col] is None:
            continue  # Continue to next iteration if error occurred

        # Select the attack method
        attack_type = select_attack_method()

        # Generate positions based on attack type
        if attack_type == "h":
            positions = generate_horizontal_positions(row, col)
        elif attack_type == "v":
            positions = generate_vertical_positions(row, col)
        elif attack_type == "c":
            positions = generate_cross_positions(row, col)
        elif attack_type == "b":  # For common bomb
            positions = [(row, col)]  # Only attack the specified position
        else:
            error_message = "Invalid attack type selected."
            continue

        # Check if all positions are valid
        if any(
            pos[0] < 0
            or pos[0] >= len(matrix)
            or pos[1] < 0
            or pos[1] >= len(matrix[0])
            for pos in positions
        ):
            error_message = "One or more positions are out of bounds."
            continue

        # Process the attacks for all positions
        for pos in positions:
            result = False
            matrix, hitted_matrix, result, message = attack(
                pos[0], pos[1], matrix, hitted_matrix
            )

            # Provide feedback on the attack result
            if result:
                print(f"Attack at {chr(pos[1] + ord('A'))}{pos[0] + 1} was a hit!")
            else:
                print(
                    f"Attack at {chr(pos[1] + ord('A'))}{pos[0] + 1} was a miss or already attacked."
                )

            # If the position has already been attacked
            if hitted_matrix[pos[0]][pos[1]] in [
                "X",
                "O",
            ]:  # Assuming 'X' is hit and 'O' is miss
                error_message = f"Position {chr(pos[1] + ord('A'))}{pos[0] + 1} has already been attacked."
            else:
                error_message = (
                    message  # Use the message from the attack function if applicable
                )

        return matrix, hitted_matrix, message


def random_attack(player_grid, player_hitted_grid):
    """
    Perform a random attack on the player's grid.

    This function randomly selects a position and an attack method to perform
    an attack on the player's grid. It ensures that the selected position has
    not been previously hit.

    Args:
        player_grid (list of list of str): The player's grid representing the positions of ships.
        player_hitted_grid (list of list of str): The grid representing the positions that have been hit.

    Returns:
        tuple: The result of the attack, as returned by the com_attack function.
    """
    attack_methods = ["h", "v", "c", "b"]  # Available attack methods
    while True:
        # Randomly select a position for the attack
        row = random.randint(0, 9)  # Assuming a 10x10 grid
        col = random.randint(0, 9)

        attack_type = random.choice(attack_methods)  # Randomly select attack method

        # Check if the attack is valid (is not already hit)
        if player_hitted_grid[row][col] not in ["X", "O"]:  # Prevents double hits
            return com_attack(row, col, player_grid, player_hitted_grid, attack_type)


def com_attack(row, col, player_grid, player_hitted_grid, attack_type):
    """
    Simulates an attack on the player's grid by the computer.

    Parameters:
    row (int): The row index for the attack.
    col (int): The column index for the attack.
    player_grid (list of list of str): The player's grid showing ship positions.
    player_hitted_grid (list of list of str): The grid showing the results of previous attacks.
    attack_type (str): The type of attack to perform. Can be "h" for horizontal bomb, "v" for vertical bomb, 
                       "c" for cross bomb, or "b" for single bomb.

    Returns:
    tuple: A tuple containing:
        - player_grid (list of list of str): The updated player's grid.
        - player_hitted_grid (list of list of str): The updated grid showing the results of previous attacks.
        - str: A message indicating the result of the attack, either "hit" or "miss".
    """
    positions = []

    # Determine the type of bomb and generate positions
    if attack_type == "h":
        print("Enemy uses Horizontal bomb!")
        positions = generate_horizontal_positions(row, col)
    elif attack_type == "v":
        print("Enemy uses Vertical bomb!")
        positions = generate_vertical_positions(row, col)
    elif attack_type == "c":
        print("Enemy uses Cross bomb!")
        positions = generate_cross_positions(row, col)
    elif attack_type == "b":
        print("Enemy uses Single bomb!")
        positions = [(row, col)]  # Only attack the specified position

    hit_occurred = False  # Track if any hits occurred

    for pos in positions:
        r, c = pos
        position_label = f"{chr(r + 65)}{c + 1}"  # Format position label (e.g., A1)

        # Check if the position is within bounds
        if 0 <= r < len(player_grid) and 0 <= c < len(player_grid[0]):
            if player_grid[r][c] != "~":  # Check for a hit
                player_hitted_grid[r][c] = "X"  # Mark as hit
                print(f"Attack at {position_label} was a hit!")
                hit_occurred = True
            else:
                player_hitted_grid[r][c] = "O"  # Mark as miss
                print(f"Attack at {position_label} was a miss!")
        else:
            print(f"Invalid attack position: row {r}, col {c}")  # Debugging output

    return player_grid, player_hitted_grid, "hit" if hit_occurred else "miss"


def attack(row, col, matrix, hitted_matrix):
    """
    Simulates an attack on the battleship game board.

    Parameters:
    row (int): The row index of the attack.
    col (int): The column index of the attack.
    matrix (list of list of str): The game board matrix representing the positions of ships.
    hitted_matrix (list of list of str): The matrix representing the positions that have been attacked.

    Returns:
    tuple: A tuple containing:
        - matrix (list of list of str): The updated game board matrix.
        - hitted_matrix (list of list of str): The updated matrix representing the positions that have been attacked.
        - bool: True if the attack was successful, False if the position was already attacked.
        - str: A message indicating the result of the attack.
    """
    if hitted_matrix[row][col] == "X" or hitted_matrix[row][col] == "O":
        return (
            matrix,
            hitted_matrix,
            False,
            "You have already attacked this position. Choose another.",
        )

    if matrix[row][col] != "~":
        hitted_matrix[row][col] = "X"
        row_label = index_to_row_label(row)
        col += 1
        return matrix, hitted_matrix, True, f"Hit a ship at {row_label}{col}!"
    else:
        hitted_matrix[row][col] = "O"
        row_label = index_to_row_label(row)
        col += 1
        return matrix, hitted_matrix, True, f"Missed at {row_label}{col}."


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


def check_attacked(matrix, row, col):
    """
    Check if a given cell in the matrix has been attacked.

    Args:
        matrix (list of list of str): The game board represented as a 2D list.
        row (int): The row index of the cell to check.
        col (int): The column index of the cell to check.

    Returns:
        bool: True if the cell has been attacked (contains "X" or "O"), False otherwise.
    """
    return matrix[row][col] in ["X", "O"]
