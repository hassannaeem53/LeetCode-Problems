class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums):
            rob_first=0
            rob_second=0
            for house in nums:
                max_robbed=max(rob_second,rob_first+house)
                rob_first=rob_second
                rob_second=max_robbed
            return max_robbed
        
        if len(nums)==1:
            return nums[0]
        
        return max(rob_linear(nums[1:]),rob_linear(nums[:-1]))
    