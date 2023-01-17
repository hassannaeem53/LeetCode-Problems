class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_ind=m-1
        nums2ind=n-1
        cur=m+n-1
        if nums1_ind==0 and nums2ind==0:
            if nums1[0]>nums2[0]:
                nums1[1]=nums1[0]
                nums1[0]=nums2[0]
                
            else:
                nums1[1]=nums2[0]
        else: 
            while nums2ind>=0:
                if nums1_ind>=0 and nums1[nums1_ind]>nums2[nums2ind]:
                    nums1[cur]=nums1[nums1_ind]
                    nums1_ind-=1
                else:
                    nums1[cur]=nums2[nums2ind]
                    nums2ind-=1
                cur-=1