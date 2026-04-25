class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        for row in board:
            c = Counter(row)
            for n in c.keys():
                if n != '.' and c[n] > 1:
                    return False
        
        
        for col in zip(*board):
            c = Counter(col)
            for n in c.keys():
                if n != '.' and c[n] > 1:
                    return False
        

        for sub_i in range(9):
            sub_board = [board[i // 3 + (sub_i // 3) * 3][i % 3 + (sub_i % 3) * 3] for i in range(9)]
            c = Counter(sub_board)
            for n in c.keys():
                if n != '.' and c[n] > 1:
                    return False
        
        return True