class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        #for i in range(len(s)-2):
        #    if len(Counter(s[i:i+3]))==3:
        #        count+=1
        #return count
        first=0
        second=1
        for i in range(2,len(s)):
            print(s[i])
            if s[first]!=s[second] and s[second]!=s[i] and s[i]!=s[first]:
                count+=1
            first,second=second,i
        return count
            