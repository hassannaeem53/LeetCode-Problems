class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        total=0
        num_fives=0
        num_tens=0
        for bill in bills:
            if bill==5:
                total+=5
                num_fives+=1
            elif bill==10:
                if num_fives==0:
                    return False
                num_fives-=1
                num_tens+=1
                total+=5
            elif bill==20:
                change = bill - 5
                if num_tens > 0 and change >= 10:
                    num_tens -= 1
                    change -= 10
                while change >= 5 and num_fives > 0:
                    num_fives -= 1
                    change -= 5
                if change != 0:
                    return False
                total+=bill
        return True
