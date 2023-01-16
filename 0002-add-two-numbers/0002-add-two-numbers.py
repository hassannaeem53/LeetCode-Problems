# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode],l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2=[]
        while l1!=None:
            arr1.append(l1.val)
            #arr1.insert(0,l1.val)
            l1=l1.next
        while l2!=None:
            arr2.append(l2.val)
            #arr2.insert(0,l2.val)
            l2=l2.next
        result=[]
        carry=0
        if len(arr2)>=len(arr1):
            for i in range(len(arr2)):
                if i >= len(arr1):
                    num=carry+arr2[i]
                else:
                    num=carry+arr2[i]+arr1[i]
                if num<10:
                    result.append(num)
                    carry=0
                else:
                    carry=1
                    num=num%10
                    result.append(num)
        else:
            for i in range(len(arr1)):
                if i >= len(arr2):
                    num=carry+arr1[i]
                else:
                    num=carry+arr2[i]+arr1[i]
                if num<10:
                    result.append(num)
                    carry=0
                else:
                    carry=1
                    num=num%10
                    result.append(num)
        if carry==1:
            result.append(1)
        cur = ListNode()
        dummy=cur
        for e in result:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next

