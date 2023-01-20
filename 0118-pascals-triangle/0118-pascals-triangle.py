class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1],[1,1]]
        for i in range(2,numRows+1):
            row=[1]
            for j in range (1,i-1):
                row.append(result[i-1][j-1]+result[i-1][j])
            row.append(1)
            result.append(row)
        del result[1]
        return result
        
        
                