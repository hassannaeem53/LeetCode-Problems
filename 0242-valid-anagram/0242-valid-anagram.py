class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt=Counter(s)
        if len(s)!=len(t):
            return False
        for l in t:
            if l in cnt.keys():
                if cnt[l]==0:
                    return False
                cnt[l]-=1
            else:
                return False
        return True