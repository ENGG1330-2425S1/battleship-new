def create_matrix(n):
    """
    Creates an n x n matrix initialized with zeros.

    Parameters:
    n (int): The size of the matrix (number of rows and columns).

    Returns:
    list: A 2D list (matrix) of size n x n filled with zeros.
    """
    return [[0 for _ in range(n)] for _ in range(n)]


def edit_matrix(matrix, row, col, value):
    """
    Edits the value at a specific position in a square matrix.

    Parameters:
    matrix (list of list of int): The square matrix to be edited.
    row (int): The row index of the position to be edited.
    col (int): The column index of the position to be edited.
    value (int): The new value to be set at the specified position.

    Returns:
    list of list of int: The updated matrix.

    Prints:
    "Invalid position!" if the specified row or column is out of bounds.
    """
    n = len(matrix)
    if 0 <= row < n and 0 <= col < n:
        matrix[row][col] = value
    else:
        print("Invalid position!")
    return matrix


def edit_all(matrix, value):
    """
    Updates all elements in a square matrix to a specified value.

    Args:
        matrix (list of list of any): A square matrix represented as a list of lists.
        value (any): The value to set for each element in the matrix.

    Returns:
        list of list of any: The updated matrix with all elements set to the specified value.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = value
    return matrix


def row_label_to_index(row_label):
    """
    Convert a row label (e.g., 'A', 'B', 'C', etc.) to a zero-based index.

    Args:
        row_label (str): The row label to convert. It should be a single alphabetical character.

    Returns:
        int: The zero-based index corresponding to the row label.

    Raises:
        ValueError: If the row label is not a single alphabetical character.
    """
    return ord(row_label.upper()) - ord("A")


def index_to_row_label(index):
    """
    Convert a zero-based index to a corresponding row label.

    Args:
        index (int): A zero-based index (0-25).

    Returns:
        str: The corresponding row label (A-Z) if the index is within the range 0-25,
             otherwise returns "Invalid index!".
    """
    if 0 <= index < 26:
        return chr(index + ord("A"))
    else:
        return "Invalid index!"


def position_to_index(position):
    """
    Convert a board position in the format 'A1', 'B2', etc. to zero-based row and column indices.

    Args:
        position (str): The board position as a string, where the first character is a letter
                        representing the row and the subsequent characters are digits representing the column.

    Returns:
        tuple: A tuple (row, col) where row is the zero-based index of the row and col is the zero-based index of the column.
    """
    row_label = position[0]
    col = int(position[1:]) - 1
    row = row_label_to_index(row_label)
    return row, col


def index_to_position(position):
    """
    Converts a matrix index to a board position.

    Args:
        position (tuple): A tuple containing the row index and column index (0-based).

    Returns:
        str: Position on the board (e.g., "A1").
    """
    row = index_to_row_label(position[0])
    col = position[1] + 1
    return f"{row}{col}"
