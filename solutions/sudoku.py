import itertools
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validateRows(board) \
               and self.validateColumns(board) \
               and self.validateBoxes(board)

    def validateRows(self, board: List[List[str]]) -> bool:
        for row in board:
            row_nums = set()
            for num in row:
                if num == '.':
                    continue
                if num in row_nums:
                    return False
                row_nums.add(num)
        return True

    def validateColumns(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col_nums = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col_nums:
                    return False
                col_nums.add(board[j][i])
        return True

    def validateBoxes(self, board):
        for i in range(3):
            for j in range(3):
                box_nums = set()
                for k in range(3):
                    for l in range(3):
                        x, y = k + 3 * i, l + 3 * j
                        if board[x][y] == '.':
                            continue
                        if board[x][y] in box_nums:
                            return False
                        box_nums.add(board[x][y])
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        def backtrack(cur_board, res_board):
            empty_p = empty_pos(cur_board)
            if not empty_p:
                for i in range(9):
                    for j in range(9):
                        res_board[i][j] = cur_board[i][j]
            else:
                i, j = empty_p[0], empty_p[1]
                for k in range(1, 10):
                    chr_k = str(k)
                    row_set = set(cur_board[i])
                    column_set = {row[j] for row in cur_board if row[j] != '.'}
                    box_set = set([cur_board[x][y] for (x, y) in
                                   itertools.product(range(int(i / 3) * 3, int(i / 3) * 3 + 3),
                                                     range(int(j / 3) * 3, int(j / 3) * 3 + 3))])
                    if chr_k not in row_set \
                            and chr_k not in column_set \
                            and chr_k not in box_set:
                        board_copy = [list(row) for row in cur_board]
                        board_copy[i][j] = chr_k
                        backtrack(board_copy, res_board)

        def empty_pos(cur_board):
            for i in range(9):
                for j in range(9):
                    if cur_board[i][j] == '.':
                        return i, j
            return None

        backtrack(board, board)


def main():
    sudoku_1 = \
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ];
    sol = Solution()

    sol.solveSudoku(sudoku_1)
    for row in sudoku_1:
        print(row)

    print(sol.isValidSudoku(sudoku_1))

    sudoku_2 = [[".", ".", ".", ".", ".", "7", ".", ".", "9"],
                [".", "4", ".", ".", "8", "1", "2", ".", "."],
                [".", ".", ".", "9", ".", ".", ".", "1", "."],
                [".", ".", "5", "3", ".", ".", ".", "7", "2"],
                ["2", "9", "3", ".", ".", ".", ".", "5", "."],
                [".", ".", ".", ".", ".", "5", "3", ".", "."],
                ["8", ".", ".", ".", "2", "3", ".", ".", "."],
                ["7", ".", ".", ".", "5", ".", ".", "4", "."],
                ["5", "3", "1", ".", "7", ".", ".", ".", "."]]
    sol.solveSudoku(sudoku_2)
    for row in sudoku_2:
        print(row)

    print(sol.isValidSudoku(sudoku_2))


if __name__ == '__main__':
    main()
