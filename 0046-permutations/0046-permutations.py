class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums)==1:
            return [nums]
        result=[]
        for i in range(len(nums)):
            first=nums[i]
            remain=nums[0:i]+nums[i+1:len(nums)]
            for j in self.permute(remain):
                result.append([first]+j)
        return result