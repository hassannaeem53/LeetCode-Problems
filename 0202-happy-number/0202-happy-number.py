class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        already=set()
        while(1):
            while n>0:
                sum+=(n%10)**2
                n=n//10
            if sum==1:
                return True
            else:
                if sum in already:
                    return False
                already.add(sum)
                n=sum
                sum=0
        
            
            