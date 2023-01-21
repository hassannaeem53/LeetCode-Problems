class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Approach 1
        #cnt=Counter(s)
        #if len(s)!=len(t):
        #    return False
        #for l in t:
        #    if l in cnt.keys():
        #        if cnt[l]==0:
        #            return False
        #        cnt[l]-=1
        #    else:
        #        return False
        #return True
        
        #Approach 2
        if sorted(s)==sorted(t):
            return True
        else:
            return False