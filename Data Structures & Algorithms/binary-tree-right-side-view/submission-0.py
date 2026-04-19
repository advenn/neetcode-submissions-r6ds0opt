# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        mapp: dict[int, int] = {}

        def helper(node, level):
            level_val = mapp.get(level)
            if level_val is None:
                mapp[level] = node.val
            if node.right: helper(node.right, level + 1)
            if node.left: helper(node.left, level + 1)
        helper(root, 0)
        return list(mapp.values())
