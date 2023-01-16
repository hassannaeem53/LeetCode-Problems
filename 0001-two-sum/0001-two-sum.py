class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for i in range(len(nums)):
            #for j in range(i+1,len(nums)):
                #if nums[i]+nums[j]==target:
                    #return [i,j]
        #return
        num_dict={}
        for i in range(len(nums)):
            num_dict[nums[i]]=i
        for i in range(len(nums)):
            val=target-nums[i]
            if val in num_dict and num_dict[val]!=i:
                return [i,num_dict[val]]