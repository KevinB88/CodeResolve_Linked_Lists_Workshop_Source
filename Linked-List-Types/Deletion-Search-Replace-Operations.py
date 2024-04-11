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

    def search(self, value):
        """Search for a value in the list. Returns True if found, else False."""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def delete(self, value):
        """Delete the first occurrence of a value in the list."""
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def replace(self, old_value, new_value):
        """Replace the first occurrence of old_value with new_value."""
        current = self.head
        while current:
            if current.value == old_value:
                current.value = new_value
                return True  # Value found and replaced
            current = current.next
        return False  # Value not found


# Example Usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print("Original List:")
    ll.print_list()

    # Search for a value
    print("Searching for 3:", ll.search(3))
    print("Searching for 5:", ll.search(5))

    # Delete a value
    ll.delete(3)
    print("After deleting 3:")
    ll.print_list()

    # Replace a value
    ll.replace(2, 5)
    print("After replacing 2 with 5:")
    ll.print_list()
