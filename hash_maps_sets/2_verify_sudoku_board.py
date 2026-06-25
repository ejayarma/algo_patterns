def verify_sudoku_board(board: list[list[int]]) -> bool:
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    sub_grid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == 0:
                continue
            if num in row_sets[r]:
                return False
            if num in col_sets[c]:
                return False
            if num in sub_grid_sets[r // 3][c // 3]:
                return False
            row_sets[r].add(num)
            col_sets[c].add(num)
            sub_grid_sets[r // 3][c // 3].add(num)
    return True

my_board_1 = [
    [3, 0, 6, 0, 5, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [1, 0, 2, 5, 0, 0, 3, 2, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [0, 3, 0, 0, 0, 8, 2, 5, 0],
    [0, 1, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 0, 0, 0],
]

my_board_2 = [
    [0, 0, 3, 0, 0, 7, 0, 6, 0],
    [9, 1, 0, 0, 0, 2, 7, 4, 0],
    [2, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 9, 0, 0, 0, 0, 0, 3, 0],
    [6, 0, 2, 8, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 5, 0, 0],
    [0, 0, 1, 0, 4, 6, 0, 0, 7],
    [8, 4, 0, 7, 0, 0, 3, 0, 0],
    [7, 2, 9, 0, 0, 0, 0, 0, 6],
]

print(verify_sudoku_board(my_board_1))
print(verify_sudoku_board(my_board_2))
