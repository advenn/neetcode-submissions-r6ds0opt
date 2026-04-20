class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

		def func(node, step) -> tuple[int, int, bool]:  # (step, value, is_target)
			# print()
			# print("start", node, step)

			# left -> current -> right
			# go left on upper nodes
			if node.left:
				# print(" -> calling left", node.left)
				step, value, found = func(node.left, step)
				# print(" <- result left", step, value, found)
				if found:
					return step, value, found

			# check current node. current node is step + 1
			# print("current", node, step)
			if step + 1 == k:
				return step + 1, node.val, True
			# return step + 1, -1, False

			if node.right:
				# print(" -> calling right", node.right)

				step, value, found = func(node.right, step + 1)
				# print(" <- result right", step, value, found)
				if found:
					return step, value, found
				else:
					return step , -1, False
			# print("end", node, step)

			return step + 1, -1, False

		step, value, found = func(root, 0)
		return value

