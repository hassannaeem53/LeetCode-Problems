class Solution:
    def jump(self, nums: List[int]) -> int:
        total=len(nums)
        jumps=[float('inf')]*total
        jumps[0]=0
        for i in range(total-1):
            for j in range(1,nums[i]+1):
                if i+j<total:
                    jumps[i+j]=min(jumps[i+j],jumps[i]+1)
        return jumps[total-1]
                    
