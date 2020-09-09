import copy
from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        # print(board)
        self.backtrace(board, 0)

        return self.result

    def backtrace(self, board, row):
        if row == len(board):  #
            self.result.append(copy.deepcopy(board))
            return
        for col in range(len(board)):
            if self.is_valid(board, row, col):
                board[row][col] = 'Q'

                self.backtrace(board, row + 1)

                board[row][col] = '.'

    def is_valid(self, board, row, col):  # 判断[row, col]放置皇后是否合法
        length = len(board)

        for j in range(length):
            if board[row][j] == 'Q' and j != col:  # 判断同行是否有其他皇后
                return False
            if board[j][col] == 'Q' and j != row:  # 判断同列是否有其他皇后
                return False

        # 判断主对角线是否有其他皇后
        for k in range(1, min(row, col) + 1):
            if board[row - k][col - k] == 'Q':
                return False

        # 判断副对角线是否有其他皇后
        for m in range(1, min(row, length - 1 - col) + 1):
            if board[row - m][col + m] == 'Q':
                return False
        return True

s = Solution()
print(s.solveNQueens(4))