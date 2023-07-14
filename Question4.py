class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head):
    # Step 1: Traverse the linked list and store characters
    chars = []
    curr = head
    while curr is not None:
        chars.append(curr.val)
        curr = curr.next

    # Step 2: Traverse the linked list again and compare characters
    curr = head
    while curr is not None:
        if curr.val != chars.pop():
            return False
        curr = curr.next

    return True


# Utility function to create a linked list from a list of characters
def createLinkedList(chars):
    head = None
    prev = None
    for char in chars:
        node = ListNode(char)
        if prev is None:
            head = node
        else:
            prev.next = node
        prev = node
    return head


# Test cases
# Example 1
head1 = createLinkedList(['R', 'A', 'D', 'A', 'R'])
print(isPalindrome(head1))  # Output: True

# Example 2
head2 = createLinkedList(['C', 'O', 'D', 'E'])
print(isPalindrome(head2))  # Output: False
