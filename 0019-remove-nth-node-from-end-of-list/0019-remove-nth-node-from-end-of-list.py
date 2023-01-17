# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        cur=head
        size=0
        while temp:
            temp=temp.next
            size+=1
        if size==n:
            return head.next
        size=size-n-1
        while size>0:
            cur=cur.next
            size=size-1
        cur.next=cur.next.next
        return head
            
            