class Solution:
	def goodNodes(self, root: TreeNode) -> int:
		self.good_nodes = 0

		def dfs(node: Optional[TreeNode], max_seen: int | float):
			if node and node.val >= max_seen:
				self.good_nodes += 1
				max_seen = node.val
			if node.right: dfs(node.right, max_seen)
			if node.left: dfs(node.left, max_seen)

		dfs(root, float("-inf"))
		return self.good_nodes
