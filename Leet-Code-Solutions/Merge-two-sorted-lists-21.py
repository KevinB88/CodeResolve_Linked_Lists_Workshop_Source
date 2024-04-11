class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    # Create a dummy node which will help in easily adding nodes to the merged list
    dummy = ListNode(-1)
    # This pointer will help us build the new merged list
    current = dummy

    # Iterate through both lists until we reach the end of one
    while list1 and list2:
        # Compare the values from both lists and add the smaller one to the merged list
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next  # Move to the next node in list1
        else:
            current.next = list2
            list2 = list2.next  # Move to the next node in list2

        current = current.next  # Move to the next node in the merged list

    # If there are remaining nodes in either list1 or list2, add them to the end of the merged list
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # The first node is dummy, so we return the next node which is the head of the merged list
    return dummy.next

# Example Usage
# This part is for demonstration and won't work without creating list1 and list2 manually
# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(5)))
# merged_head = mergeTwoLists(list1, list2)
# while merged_head:
#     print(merged_head.val, end=' ')
#     merged_head = merged_head.next
