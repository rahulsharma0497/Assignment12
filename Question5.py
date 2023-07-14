class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectAndRemoveLoop(head):
    if head is None or head.next is None:
        return

    slow = head
    fast = head

    # Detect the loop using Floyd's cycle-finding algorithm
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If no loop is found, return
    if slow != fast:
        return

    # Move slow pointer to the head and find the meeting point
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Unlink the last node to remove the loop
    fast.next = None

def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Test case
# Example 1
head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(4)
head1.next.next.next = head1.next
detectAndRemoveLoop(head1)
printLinkedList(head1)  # Output: 1 3 4

# Example 2
head2 = ListNode(1)
head2.next = ListNode(8)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)
detectAndRemoveLoop(head2)
printLinkedList(head2)  # Output: 1 8 3 4
