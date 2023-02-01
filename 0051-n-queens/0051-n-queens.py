class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board= [['.']*(n) for i in range(n)]
        colSet=set()
        negDiag=set()
        posDiag=set()
        result=[]
        def combinate(row):
            if row==n:
                newboard=[''.join(i) for i in board]
                result.append(newboard)
                return
            for col in range(n):
                if col in colSet or row+col in posDiag or row-col in negDiag:
                    continue
                
                colSet.add(col)
                negDiag.add(row-col)
                posDiag.add(row+col)
                board[row][col]='Q'
                
                combinate(row+1)
                
                colSet.remove(col)
                negDiag.remove(row-col)
                posDiag.remove(row+col)
                board[row][col]='.'
        
        combinate(0)
        return result