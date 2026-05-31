"""
Problem : Reverse Linked List
Difficulty : Easy
Link :- https://leetcode.com/problems/reverse-linked-list/

Approach:
- We need to reverse the direction of every link in the linked list.
- Keep track of three pointers:
    - prev: points the previous node.
    - current: points to the current node.
    - next_node: stores the next node before changing links.
- Traverse the list one node at a time.
- For each node:
    - Save the next node.
    - Reverse the current node's pointer to point to the previous node.
    - Move prev pointer to current
    - Move current one step forward.
- Continue until current becomes None.
- At the end:
    - prev will point to the new head of the reversed list.
- Return prev.

Complexity
- Time  : O(n)
- Space : O(1)

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        prev = None
        current = head

        while current:

            next_node = current.next

            current.next = prev

            prev = current
            current = next_node

        return prev


def create_linked_list(values):

    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):

    current = head

    while current:
        end_char = '->' if current.next else '\n'
        print(current.val, end=end_char)
        current = current.next



if __name__ == "__main__":

    solution = Solution()

    head1 = create_linked_list([1, 2, 3, 4, 5])  # Linked list
    reversed_head1 = solution.reverseList(head1) # revers linked list
    print_linked_list(reversed_head1)            # print reversed linked list

