"""
Problem : Merge Two Sorted Lists
Difficulty : Easy
Link :- https://leetcode.com/problems/merge-two-sorted-lists/

Approach:
- Given two sorted linked lists.
- Since both lists are already sorted, compare the current nodes from both lists.
- The smaller value should be added to the merged list first.
- Use a dummy node to simplify handling the head of the merged list.
- Maintain a current pointer that always points to the last node of the merged list.
- While both lists have nodes:
    - Compare the values of list1 and list2.
    - Attach the smaller node to the merged list.
    - Move the pointer of the list from which the node was taken.
    - Move the current pointer forward.
- After the loop:
    - One list may still contain remaining nodes.
    - Since the remaining nodes are already sorted, attach them directly.
- Return dummy.next because dummy is only a helper node.

Complexity
- Time  : O(n + m)
- Space : O(1)

  - n = length of list1
  - m = length of list2

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(
            self, 
            list1: ListNode | None,
            list2: ListNode | None
            ) -> ListNode | None :
        
        dummy = ListNode()
        current = dummy

        while list1 and list2:

            if list1.val < list2.val:

                current.next = list1
                list1 = list1.next
            
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        if list1:
            current.next = list1
        
        if list2:
            current.next = list2
        
        return dummy.next
            


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

    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])

    merged = solution.mergeTwoLists(list1, list2)
    print_linked_list(merged)