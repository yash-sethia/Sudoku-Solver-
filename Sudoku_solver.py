def print_sudoku(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end = '')
        print('\n')


def empty_space(arr, l):
    for i in range(9):
        for j in range(9):
            if(arr[i][j] == 0):
                l[0] = i
                l[1] = j
                return True
    else:
        return False


def check_row(arr, row, num):
    for j in range(9):
        if arr[row][j] == num:
            return False
    return True



def check_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return False
    return True



def check_grid(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[row + i][col + j] == num:
                return False
    return True



def solve_sudoku(arr):
    l = [0, 0]
    if not empty_space(arr, l):
        return True
    else:
        row = l[0]
        col = l[1]
        for k in range(1, 10):
            num = k
            if check_row(arr, row, num) and check_col(arr, col, num) and check_grid(arr, row - (row%3), col - (col%3), num):
                arr[row][col] = k
                if solve_sudoku(arr):
                    return True
                arr[row][col] = 0

        return False


if __name__ == "__main__":
    grid = [[0 for x in range(9)] for y in range(9)]

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solve_sudoku(grid):
        print(' Sudoku Solved ')
        print_sudoku(grid)
    else:
        print("Sudoku can't be solved")











