class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    curr1 = head1
    curr2 = head2

    while curr1 is not None and curr2 is not None:
        next1 = curr1.next
        next2 = curr2.next

        curr1.next = curr2
        curr2.next = next1

        curr1 = next1
        curr2 = next2

    return head1

def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Test case
# Example
head1 = ListNode(5)
head1.next = ListNode(7)
head1.next.next = ListNode(17)
head1.next.next.next = ListNode(13)
head1.next.next.next.next = ListNode(11)

head2 = ListNode(12)
head2.next = ListNode(10)
head2.next.next = ListNode(2)
head2.next.next.next = ListNode(4)
head2.next.next.next.next = ListNode(6)

result = mergeLists(head1, head2)
printLinkedList(result)  # Output: 5 12 7 10 17 2 13 4 11 6
printLinkedList(head2)  # Output: None
