class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        a="hassan"
        if len(s)>12:
            return []
        result=[]
        
        def recur(s_index,dots,cur):
            if s_index==len(s) and dots==4:
                result.append(cur[:-1])
                return
            if dots>4:
                return
            
            for i in range(s_index,min(s_index+3,len(s))):
                if int(s[s_index:i+1])<256 and (s_index==i or s[s_index]!="0"):
                    recur(i+1,dots+1,cur+s[s_index:i+1]+'.')
        
        recur(0,0,"")
        return result
                
                
            
            