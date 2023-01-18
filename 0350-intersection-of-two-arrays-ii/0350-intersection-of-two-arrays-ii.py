class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size1,size2=len(nums1),len(nums2)
        result=[]
        flags=[False for x in range(len(nums1))]
        for i in range(size2):
            for j in range(size1):
                if nums1[j]==nums2[i] and flags[j]==False:
                    result.append(nums1[j])
                    flags[j]=True
                    break
        return result
                    
            