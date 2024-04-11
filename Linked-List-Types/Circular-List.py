import time


class ListNode:
    """A node in a circular linked list."""

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class CircularLinkedList:
    """A circular linked list."""

    def __init__(self):
        self.head = None

    def append(self, value):
        """Append a new value to the list, maintaining circularity."""
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Point back to itself to maintain circularity
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Complete the circle by pointing to the head

    def print_list(self, cycles=3):
        """Print the list, cycling through it 'cycles' times."""
        if not self.head:
            return

        current = self.head
        start_value = self.head.value
        visited = 0

        while visited < cycles:
            print(current.value, end=' ')
            time.sleep(1)  # Delay to show the cycling nature
            current = current.next
            if current.value == start_value:
                visited += 1
                print("| Cycle:", visited, "|", end=' ')
        print("\nDone.")


# Example Usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)

    print("Cycling through the list:")
    cll.print_list()
