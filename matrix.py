# Function to create an n x n matrix
def create_matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]


# Function to edit the n x n matrix at a specific position
def edit_matrix(matrix, row, col, value):
    n = len(matrix)
    if 0 <= row < n and 0 <= col < n:
        matrix[row][col] = value
    else:
        print("Invalid position!")
    return matrix


# Function to edit all vaules in the n x n matrix
def edit_all(matrix, value):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = value
    return matrix


# Row (A-Z) convert to index (0-25)
def row_label_to_index(row_label):
    return ord(row_label.upper()) - ord("A")


# Index (0-25) convert to row (A-Z)
def index_to_row_label(index):
    if 0 <= index < 26:
        return chr(index + ord("A"))
    else:
        return "Invalid index!"
