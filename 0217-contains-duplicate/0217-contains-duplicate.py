class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # #solution:1
        # nums=sorted(nums)
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False
        
        if len(set(nums))!=len(nums):
            return True
        return False