class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodes(head, M, N):
    if head is None or M <= 0 or N <= 0:
        return head

    curr = head
    count = 1

    while curr is not None:
        if count < M:
            count += 1
        else:
            for _ in range(N):
                if curr.next is not None:
                    curr.next = curr.next.next
                else:
                    break
        curr = curr.next
        count += 1

    return head

def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.val, end=" ")
        curr = curr.next
    print()

# Test case
# Example
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
M = 2
N = 2
result = deleteNodes(head, M, N)
printLinkedList(result)  # Output: 1 2 5 6 9
