# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, min_val, max_val) -> bool:
            if not node:
                return True
            if not (min_val < node.val <max_val):
                return False
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)

            # left = False
            # right = False
            # if node.left:
            #     left = node.val > node.left.val and node.left.val > min_val
            # else:
            #     left = True
            # if node.right:
            #     right = node.val < node.right.val and node.right.val < max_val
            # else:
            #     right = True
            # return left and right and validate(node.left, float("-inf"), node.val) and validate(node.right, node.val, float("inf"))
        
        return validate(root, float("-inf"), float("inf"))

            # if node.left and node.right: 
            #     if node.left.val < node.val < node.right.val:
            #         left = validate(node.left)
            #         right = validate(node.right)
            #         return left and right
            #     else:
            #         return False
            # if node.left:
            #     if not node.right:

            #         left = validate(node.left)
            #         return left
                