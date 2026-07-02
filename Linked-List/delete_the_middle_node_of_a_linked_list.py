"""
Problem : Delete the Middle Node of a Linked List
Difficulty : Medium
Link : https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Approach:
- If the list contains only one node, return None.
- Use two pointers:
    - slow moves one step at a time.
    - fast moves two steps at a time.
- Keep track of the node before slow using a prev pointer.
- When fast reaches the end, slow points to the middle node.
- Delete the middle node by connecting prev.next to slow.next.
- Return the head of the modified linked list.

Complexity
- Time  : O(n)
- Space : O(1)

"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None
        
        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next

        return head


def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:

        current.next = ListNode(value)
        current = current.next
    
    return dummy.next

def print_linked_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next
    
    print(result)


if __name__ == "__main__":
    
    sol = Solution()

    head = build_linked_list([1,3,4,7,1,2,6])
    sol.deleteMiddle(head)
    print_linked_list(head)

    head2 = build_linked_list([1,2,3,4])
    sol.deleteMiddle(head2)
    print_linked_list(head2)
