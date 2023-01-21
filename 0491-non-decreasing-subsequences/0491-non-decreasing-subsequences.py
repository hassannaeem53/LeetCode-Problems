class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        seq=[]
        result=set()
        def findSub(index):
            if index==len(nums):
                if len(seq)>=2:
                    result.add(tuple(seq))
                return
            if not seq or seq[-1]<=nums[index]:
                seq.append(nums[index])
                #print(seq)
                findSub(index+1)
                seq.pop()
            
            findSub(index+1)   
        findSub(0)
        return (result)