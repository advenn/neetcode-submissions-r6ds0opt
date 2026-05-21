
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        node = head
        clones = {}
        while node:
            node_cloned = clones.get(node)
            if not node_cloned:
                node_cloned = Node(x=node.val)
            clones[node] = node_cloned

            node_random = node.random
            node_next = node.next

            cloned_next = None
            if node_next:
                cloned_next = clones.get(node_next)
                if cloned_next is None:
                    cloned_next = Node(x=node_next.val)
            clones[node].next = cloned_next
            if node.next and clones.get(node.next) is None:
                clones[node.next] = cloned_next

            cloned_random = None
            if node_random:
                cloned_random = clones.get(node_random)
                if not cloned_random:
                    cloned_random = Node(x=node_random.val)
            clones[node].random = cloned_random

            if node.random and clones.get(node.random) is None:
                clones[node.random] = cloned_random

            node = node.next
        return clones[head]
