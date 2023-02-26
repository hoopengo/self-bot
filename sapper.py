import random


def generate_minesweeper_board():
    """
    Generates a Minesweeper game board as a string.

    Returns:
        A string representation of a Minesweeper game board.
    """
    # Mapping of counts to emojis
    views = {
        0: ":white_large_square:",
        1: ":one:",
        2: ":two:",
        3: ":three:",
        4: ":four:",
        5: ":five:",
        6: ":six:",
        7: ":seven:",
        8: ":eight:",
        9: ":nine:",
        10: ":keycap_ten:",
    }

    # Initialize game board with empty cells
    rows, cols = 4, 7
    table = [[":white_large_square:"] * cols for _ in range(rows)]

    # Place bombs randomly on the board
    bomb_indices = random.sample(range(rows * cols), 4)
    for bomb_index in bomb_indices:
        row, col = bomb_index // cols, bomb_index % cols
        table[row][col] = ":bomb:"

    # Count the number of bombs surrounding each cell and update with appropriate emoji
    for row_idx, row in enumerate(table):
        for col_idx, cell in enumerate(row):
            if cell == ":bomb:":
                # Skip counting for cells containing bombs
                continue

            count = 0
            for i in range(max(0, row_idx - 1), min(row_idx + 2, rows)):
                for j in range(max(0, col_idx - 1), min(col_idx + 2, cols)):
                    if table[i][j] == ":bomb:":
                        count += 1

            table[row_idx][col_idx] = views[count]

    # Format the board as a string and return
    sapper = ""
    for row in table:
        sapper += "".join([f"||{cell}||" for cell in row]) + "\n"

    return sapper
