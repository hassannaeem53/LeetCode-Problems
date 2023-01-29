class Solution:
    def countSubstrings(self, s: str) -> int:
        def palindroms_count(s,offset):
            count=0
            for i in range(len(s)):
                left,right=i,i+offset
                while left>=0 and right<len(s) and s[left]==s[right]:
                    count+=1
                    left-=1
                    right+=1
            return count
                    
        return palindroms_count(s,1)+ palindroms_count(s,0)
        