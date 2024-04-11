class ListNode:
    """A node in a singly-linked list."""
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """A singly-linked list."""
    def __init__(self):
        self.head = None

    def append(self, value):
        """Append a new value to the end of the list."""
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def print_list(self):
        """Print all values of the list."""
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()  # For newline at the end


# Example Usage
if __name__ == "__main__":
    # Create a linked list and add some elements
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # Print the list
    ll.print_list()
