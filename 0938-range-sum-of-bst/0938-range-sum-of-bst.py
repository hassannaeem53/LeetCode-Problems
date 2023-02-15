# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res=0
        def inOrder(r):
            nonlocal res
            if not r:
                return
            if r.val>=low:
                inOrder(r.left)
            if r.val>=low and r.val<=high:
                res+=r.val
            if r.val<=high:
                inOrder(r.right)
    
        inOrder(root)
        return res
