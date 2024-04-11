class ListNode:
    """A node in a doubly-linked list."""

    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """A doubly-linked list."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """Append a new value to the end of the list."""
        new_node = ListNode(value)
        if not self.head:  # If the list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def print_list(self):
        """Print all values of the list forwards."""
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next
        print()  # For newline at the end

    def print_list_backwards(self):
        """Print all values of the list backwards."""
        current = self.tail
        while current:
            print(current.value, end=' ')
            current = current.prev
        print()  # For newline at the end


# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    print("Print forwards:")
    dll.print_list()

    print("Print backwards:")
    dll.print_list_backwards()
