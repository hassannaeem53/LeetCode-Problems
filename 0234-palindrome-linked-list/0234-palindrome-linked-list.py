# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#For middle value detection used Floyd Cycle Algo
#reversing only second half of the list 
#comparing first half list with reversed second half

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:   #Floyd's Cycle Detection Algorithm
            slow=slow.next
            fast=fast.next.next
        
        prev,slow,prev.next=slow,slow.next,None
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        fast,slow=head,prev
            
        while slow:
            if slow.val!=fast.val:
                return False
            else:
                slow=slow.next
                fast=fast.next
        return True
            
        