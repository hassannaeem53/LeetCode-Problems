class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index=-1
        for i in range(len(matrix)):
            if (matrix[i][-1]==target):
                return True
            if (matrix[i][-1]>target):
                index=i
                break
        for i in range(len(matrix[index])):
            print(matrix[index][i])
            if matrix[index][i]==target:
                return True
        return False