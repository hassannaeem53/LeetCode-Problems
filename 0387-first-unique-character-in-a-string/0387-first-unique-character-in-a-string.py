class Solution:
    def firstUniqChar(self, s: str) -> int:
        #Approach 1
        #for i,l in enumerate(s):
        #    if s.count(l)==1:
        #        return i
        #return -1
        
        #Approach 2
        count=dict()
        for i in s:
            if i in count:
                count[i]=count[i]+1
            else:
                count[i]=0
        for i,j in enumerate(s):
            if count[j]==0:
                return i
        return -1