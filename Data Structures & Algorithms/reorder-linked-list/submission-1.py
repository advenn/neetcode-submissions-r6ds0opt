class Solution:

	def reorderList(self, head: Optional[ListNode]) -> None:
		slow, fast = head, head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		second = slow.next
		slow.next = None

		stack = []
		start = head
		while second:
			stack.append(second)
			second = second.next

		while stack and start.next:
			next = start.next
			last_item = stack.pop()
			last_item.next = next
			start.next = last_item
			start = next