class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    # Create a dummy node that points to the head of the list
    dummy = ListNode(next=head)
    # 'prev' starts at the dummy node, and 'current' starts at the actual head of the list
    prev, current = dummy, head

    # Traverse the list
    while current:
        if current.val == val:
            # Skip the current node by rewiring the 'next' pointer of the 'prev' node
            prev.next = current.next
        else:
            # Move 'prev' forward only if we're not removing the current node
            prev = current
        # Move 'current' forward in either case
        current = current.next

    # Return the new head, which might have changed if the original head was removed
    return dummy.next

# Example Usage
# This part is for demonstration and won't work without creating a linked list manually
# head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
# new_head = removeElements(head, 6)
# while new_head:
#     print(new_head.val, end=' ')
#
