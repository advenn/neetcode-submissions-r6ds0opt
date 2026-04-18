class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		dummy = ListNode(0, head)

		left, right = dummy, head
		cnt = 0

		while right and cnt < n:
			right = right.next
			cnt += 1
		# printList(left)
		# printList(right)

		while right:
			right = right.next
			left = left.next
		left.next = left.next.next
		return dummy.next