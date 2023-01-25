# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def rec(r):
            if not r:
                return
            else:
                rec(r.left)
                res.append(r.val)
                rec(r.right)
        rec(root)
        return res