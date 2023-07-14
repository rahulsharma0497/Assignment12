class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isCircular(head):
    if head is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

# Test cases
# Example 1: Circular linked list
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = head1  # Connect the last node to the head
print(isCircular(head1))  # Output: True

# Example 2: Non-circular linked list
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
print(isCircular(head2))  # Output: False
