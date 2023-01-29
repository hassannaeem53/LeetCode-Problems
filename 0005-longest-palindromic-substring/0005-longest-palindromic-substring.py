class Solution:
    def longestPalindrome(self, s: str) -> str:
        def longestsubstring(s,offset):
            substring=""
            max_substring_len=0
            for i in range(len(s)):
                left,right=i,i+offset
                while left>=0 and right<len(s) and s[left]==s[right]:
                    if right-left+1>max_substring_len:
                        substring=s[left:right+1]
                        max_substring_len=right-left+1
                    left-=1
                    right+=1
            return substring
                    
        e=longestsubstring(s,1)
        o=longestsubstring(s,0)
        
        return e if len(e)>len(o) else o