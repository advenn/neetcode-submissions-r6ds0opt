class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        intermediary = 0
        head = ListNode(0)
        last = head
        while l1 or l2 or intermediary:
            s = 0

            if l1:
                s += l1.val
            if l2:
                s += l2.val

            if intermediary:
                s += intermediary

            intermediary, s = divmod(s, 10)

            node = ListNode(s)

            last.next = node
            last = last.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next
