# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(first, second) -> bool:
            if first and second and first.val == second.val:
                left = helper(first.left, second.left)
                right = helper(first.right, second.right)
                return left and right
            if not first and not second:
                return True
            return False
        return helper(p,q)


