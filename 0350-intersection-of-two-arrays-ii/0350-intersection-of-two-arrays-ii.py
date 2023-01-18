class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ##Approach 1
        #size1,size2=len(nums1),len(nums2)
        #result=[]
        #flags=[False for x in range(len(nums2))]
        #for i in range(size1):
        #    for j in range(size2):
        #        if nums1[i]==nums2[j] and flags[j]==False:
        #            result.append(nums1[i])
        #            flags[j]=True
        #            break
        #return result
        
        #Approach2
        result=[]
        cnt=Counter(nums1)
        for num in nums2:
            if cnt[num]>0:
                result.append(num)
                cnt[num]-=1
        return result
                    
            