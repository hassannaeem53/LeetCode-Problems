class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        o_row=len(mat)
        o_col=0
        for i in mat:
            o_col+=len(i)
        if(o_col==r*c):
            o_r=0
            o_c=0
            result=[[0 for j in range(c)] for i in range(r)]
            for i in range(r):
                for j in range(c):
                    if o_c== len(mat[o_r]):
                        o_r+=1
                        o_c=0
                    result[i][j]=mat[o_r][o_c]
                    print(result[i][j])
                    o_c+=1
            return result
        else:
            return mat
                    