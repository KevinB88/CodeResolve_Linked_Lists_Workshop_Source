class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddleNode(head):
    tortoise = head  # This pointer moves one step at a time
    hare = head      # This pointer moves two steps at a time

    while hare and hare.next:
        tortoise = tortoise.next       # Move tortoise one step
        hare = hare.next.next          # Move hare two steps

    # When hare reaches the end of the list, tortoise will be at the middle
    return tortoise

# Example Usage
# This part is for demonstration and won't work without creating a linked list manually
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# middle_node = findMiddleNode(head)
# print(middle_node.val)  # Output will be 3 for this example
