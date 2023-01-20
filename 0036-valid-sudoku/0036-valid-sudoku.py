def isValid(mylist):
    return False if [x for x in mylist if mylist.count(x) > 1 and x!='.'] else True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            if isValid(i)==False:
                return False
        board = [[board[j][i] for j in range(9)] for i in range(9)]
        for i in board:
            if isValid(i)==False:
                        return False
        temp_arr=[]
        arr=[]
        for num in range(0,9,3): # division matrix to 3 columns 3x9
                for col in board:
                    temp_arr.append(col[num:num+3])
        for num in range(0,27,3): # division columns to 9 blocks 3x3
            arr.append(temp_arr[num:num+3])
        for i in arr:
            block=i[0]+i[1]+i[2]
            if isValid(block)==False:
                return False
        return True