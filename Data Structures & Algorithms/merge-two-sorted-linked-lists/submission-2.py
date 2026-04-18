
class Solution:
	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

		heap = []
		for i, node in enumerate((list1, list2)):
			if node:
				heapq.heappush(heap, (node.val, i, node))

		dummy = ListNode(0)
		curr = dummy

		while heap:
			val, i, node = heapq.heappop(heap)
			curr.next = node
			curr = curr.next
			if node.next:
				heapq.heappush(heap, (node.next.val, i, node.next))
		return dummy.next

