# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=ListNode(next=head)
        prev=temp
        cur=head
        while cur and cur.next:
            prev.next=cur.next
            cur.next=cur.next.next
            prev.next.next=cur
            prev,cur=cur,cur.next
        return temp.next