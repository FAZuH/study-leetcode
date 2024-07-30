from typing import *  # type: ignore


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check column validity
        column_value_existence = [[False] * 9 for _ in range(9)]
        """Existence of nth-digit within i-th column"""
        row_value_existence = [[False] * 9 for _ in range(9)]
        """the existence of nth-digit within j-th column"""

        for row_i in range(9):
            for col_i in range(9):
                entry = board[row_i][col_i]
                if entry == '.': continue
                entry = int(entry) - 1

                if row_value_existence[row_i][entry] is True:
                    return False
                if column_value_existence[col_i][entry] is True:
                    return False

                row_value_existence[row_i][entry] = True
                column_value_existence[col_i][entry] = True

        for i in range(3):
            for j in range(3):
                subbox = self.getSubbox(i, j, board)
                if self.isValidSubbox(subbox) is False:
                    return False

        return True

    def getSubbox(self, i: int, j: int, board: List[List[str]]) -> List[List[str]]:
        left_row_idx = (0 + i) * 3
        right_row_idx = left_row_idx + 3
        left_col_idx = (0 + j) * 3
        right_col_idx = left_col_idx + 3
        rows = board[left_row_idx:right_row_idx]
        subbox = [row[left_col_idx:right_col_idx] for row in rows]
        return subbox

    def isValidSubbox(self, subbox: List[List[str]]) -> bool:
        value_existence = [False] * 9
        for row in subbox:
            for entry in row:
                if entry == '.': continue
                entry = int(entry) - 1
                if value_existence[entry] is True:
                    return False
                value_existence[entry] = True
        return True


class NeetSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


obj = Solution()
ret = obj.isValidSudoku(
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
)
print(ret, 'hi')
