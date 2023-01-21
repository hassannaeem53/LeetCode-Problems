class Solution:
    def frequencySort(self, s: str) -> str:
        cnt=Counter(s)
        cnt=dict(sorted(cnt.items(), key=lambda item: item[1], reverse=True))
        ns=''
        for k,v in cnt.items():
            for i in range(v):
                ns+=k
        return ns