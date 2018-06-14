class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for _ in range(len(board))]
        cols = [[] for _ in range(len(board))]
        subMatrices = [[] for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num != ".":
                    if num not in rows[i] and num not in cols[j] and num not in subMatrices[3 * (i // 3) + (j // 3)]:
                        rows[i].append(num)
                        cols[j].append(num)
                        subMatrices[3 * (i // 3) + (j // 3)].append(num)
                    else:
                        return False

        return True