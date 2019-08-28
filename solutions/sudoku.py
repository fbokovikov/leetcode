from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_rows = self.validateRows(board);
        if not valid_rows:
            return False
        valid_columns = self.validateColumns(board)
        if not valid_columns:
            return False
        valid_boxes = self.validateBoxes(board)
        if not valid_boxes:
            return False
        return True

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
        N = len(board)
        for i in range(N):
            col_nums = set()
            for j in range(N):
                if board[j][i] == '.':
                    continue
                if board[j][i] in col_nums:
                    return False
                col_nums.add(board[j][i])
        return True

    def validateBoxes(self, board):
        N = len(board)
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


def main():
    sudoku_1 = \
        [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
];
    sudoku_2 = \
    [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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

    print(sol.isValidSudoku(sudoku_1))
    print(sol.isValidSudoku(sudoku_2))

if __name__ == '__main__':
    main()
