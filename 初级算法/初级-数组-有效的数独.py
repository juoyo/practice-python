class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for i in range(9)]
        col = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    box_index = (i // 3) * 3 + j // 3

                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                    if row[i][num] > 1 or col[j][num] > 1 or boxes[box_index][num] > 1:
                        return False
        return True

