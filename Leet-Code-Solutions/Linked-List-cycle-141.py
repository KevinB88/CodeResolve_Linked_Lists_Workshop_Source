class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    if not head:
        return False

    tortoise = head  # This pointer moves one step at a time
    hare = head      # This pointer moves two steps at a time

    while hare and hare.next:
        tortoise = tortoise.next       # Move tortoise one step
        hare = hare.next.next          # Move hare two steps

        if tortoise == hare:           # If they meet, there's a cycle
            return True

    # If hare reaches the end (hare or hare.next is null), there's no cycle
    return False