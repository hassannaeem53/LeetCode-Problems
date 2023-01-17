# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz, ptr = 0, head
        
        while ptr:
            ptr = ptr.next
            sz+=1

        if n==sz:
            return head.next

        sz -= n+1
        ptr = head 
          
        while sz > 0:
            ptr = ptr.next
            sz-=1
            
        ptr.next = ptr.next.next   
        
        return head
            
            