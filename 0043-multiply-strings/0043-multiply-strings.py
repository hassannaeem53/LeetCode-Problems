class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        num1=num1[::-1]
        num2=num2[::-1]
        f_result=0
        def addreverse(res):
            sum=0
            for i in range(len(res)):
                     sum+=(res[i]*(10**i))
            return f_result+sum
        
        for zeros,i in enumerate(num2):
            mul=0
            result=[]
            for z in range(zeros):
                result.append(0)
            carry=0
            for j in num1:
                mul=(int(i)*int(j))+carry
                carry=mul//10
                result.append(mul%10)
            if carry!=0:
                result.append(carry)
            f_result=addreverse(result)
            
        def IntToStr(res):
            result=""
            while res>0:
                rem = res % 10
                res = res//10
                result = str(rem)+result
            return result
    
        return IntToStr(f_result)

        

                    
                    
                    