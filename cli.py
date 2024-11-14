import os


def matrix_output_preprocess(matrix):
    result = []

    if matrix == []:
        return ""

    # Add column labels
    result.append("  " + " ".join(f"{i:2}" for i in range(1, len(matrix[0]) + 1)))

    # Add each row with row labels (A-Z)
    for i, row in enumerate(matrix):
        row_label = chr(ord("A") + i)
        result.append(f"{row_label}  " + " ".join(f"{cell:2}" for cell in row))

    return "\n".join(result)


# Clear the console
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
