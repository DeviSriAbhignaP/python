class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

values = [1, 2, 3, 4, 5]
head = create_linked_list(values)

print("Original List:")
print_linked_list(head)


solution = Solution()
reversed_head = solution.reverseList(head)

print("Reversed List:")
print_linked_list(reversed_head)
