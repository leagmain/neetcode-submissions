class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        sqr = defaultdict(list)

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == '.':
                    continue
                if n in row[r] or n in col[c] or n in sqr[(r // 3,c // 3)]:
                    return False
                row[r].append(n)
                col[c].append(n)
                sqr[(r // 3,c // 3)].append(n)
        return True