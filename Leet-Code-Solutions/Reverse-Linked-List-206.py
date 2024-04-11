class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None  # Previous node starts as None
    current = head  # Current node starts as the head of the list

    while current:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move prev to current node
        current = next_node  # Move current to the next node (stored earlier)

    # At the end, prev will be the new head of the reversed list
    return prev

# Example Usage
# This part is for demonstration and won't work without creating a linked list manually
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# reversed_head = reverseList(head)
# while reversed_head:
#     print(reversed_head.val, end=' ')
#     reversed_head = reversed_head.next
