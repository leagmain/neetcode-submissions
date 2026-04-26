class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        for i in range(9):
            c = Counter(board[i])
            for n in c.keys():
                if n != '.' and c[n] > 1:
                    return False
            
            c.clear()
            col = [board[j][i] for j in range(9)]
            c.update(col)
            for n in c.keys():
                if n != '.' and c[n] > 1:
                    return False

            c.clear()
            sub_board = [board[j // 3 + (i // 3) * 3][j % 3 + (i % 3) * 3] for j in range(9)]
            c.update(sub_board)
            for n in c.keys():
                if n != '.' and c[n] > 1:
                    return False
        
        return True