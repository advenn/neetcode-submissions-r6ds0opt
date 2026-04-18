class Solution:

	def reorderList(self, head: Optional[ListNode]) -> None:
		slow, fast = head, head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next

		# printList(slow)
		second = slow.next
		slow.next = None

		# print("start")
		# printList(head)
		# # printList(slow)
		# printList(fast)
		# printList(second)
		# print("end")
		stack = []
		start = head
		# half = slow
		while second:
			stack.append(second)
			second = second.next

		# for o in stack:
		# 	printList(o)

		while stack and start.next:
			next = start.next
			last_item = stack.pop()
			last_item.next = next
			start.next = last_item
			start = next