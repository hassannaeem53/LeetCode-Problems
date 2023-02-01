class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Row,Col= len(board),len(board[0])
        
        def dfs(row,col,cur):
            if cur==len(word):
                return True
            
            if row>=Row or col>=Col or board[row][col]!=word[cur] \
            or row<0 or col<0 or board[row][col]=='#':
                return False
            
            temp=board[row][col]
            board[row][col]='#'
            
            flag= (dfs(row+1,col,cur+1) or 
                   dfs(row,col+1,cur+1) or
                   dfs(row-1,col,cur+1) or
                   dfs(row,col-1,cur+1)) 
            
            board[row][col]=temp
            return flag
        
        for i in range(Row):
            for j in range(Col):
                if dfs(i,j,0):
                    return True
        return False