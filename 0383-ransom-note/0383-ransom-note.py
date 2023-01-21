class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt=Counter(magazine)
        for l in ransomNote:
            if l in cnt.keys():
                if cnt[l]==0:
                    return False
                cnt[l]-=1
            else:
                return False
        return True