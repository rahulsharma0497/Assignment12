class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getNthFromEnd(head, n):
    if head is None:
        return None

    slow = head
    fast = head

    # Move the fast pointer N steps ahead
    for _ in range(n):
        if fast is None:
            return None
        fast = fast.next

    # Move both pointers until the fast pointer reaches the end
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.val

# Test case
# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
head1.next.next.next.next.next.next = ListNode(7)
head1.next.next.next.next.next.next.next = ListNode(8)
head1.next.next.next.next.next.next.next.next = ListNode(9)
n1 = 2
print(getNthFromEnd(head1, n1))  # Output: 8

# Example 2
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(5)
n2 = 5
print(getNthFromEnd(head2, n2))  # Output: 1
