class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        size1,size2=len(nums1),len(nums2)
        result=[]
        flags=[False for x in range(len(nums2))]
        for i in range(size1):
            for j in range(size2):
                if nums1[i]==nums2[j] and flags[j]==False:
                    result.append(nums1[i])
                    flags[j]=True
                    break
        return result
                    
            