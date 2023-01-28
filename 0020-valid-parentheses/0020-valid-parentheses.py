class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for l in s:
            if l=='(' or l=='[' or l=='{':
                stack.append(l)
            else:
                if not stack:
                    return False
                p=stack.pop()
                if (p=='[' and l!=']') or (p=='{' and l!='}') or (p=='(' and l!=')'):
                    return False
        if len(stack)>0:
            return False
        return True
            