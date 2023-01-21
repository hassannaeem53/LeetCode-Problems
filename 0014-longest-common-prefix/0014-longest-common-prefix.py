class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        target=strs.pop(0)
        match=""
        max_match=1000
        for word in strs:
            match=0
            for j in range(len(target)):
                if j<len(word) and target[j]==word[j]:
                    match+=1
                else:
                    if max_match>match:
                        max_match=match
                        break
        return target[0:max_match]
                