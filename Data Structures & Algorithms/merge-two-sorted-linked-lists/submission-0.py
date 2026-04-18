# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            node = list2
            list2 = list2.next
        else:
            node = list1
            list1 = list1.next
        head = node
        while list1 or list2:  
            if not list1:
                node.next = list2
                return head
            if not list2:
                node.next = list1
                return head
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        return head