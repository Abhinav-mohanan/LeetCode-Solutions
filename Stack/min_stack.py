"""
Problem : Min Stack
Difficulty : Medium
Link :- https://leetcode.com/problems/min-stack/

Approach:
- Maintain two standard stacks : 
    one main stack to hold all elements, 
    and a secondary tracking stack ('min_stack') to keep track of the minimum values.
- When pushing a new element : 
    compare it with the current top of 'min_stack'. 
    Push the smaller of the two onto 'min_stack' so its top always the minimum value.
- When popping, 
    remove the top element from both stacks simultaneously.

Complexity
- Time  : O(1) 
- Space : O(n)

"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)

        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    min_stack = MinStack()

    # Pushing elements : [-2, 0, -3]
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)

    # Get current minimum
    print(f'Current Minimum : {min_stack.getMin()}')
    
    # popping top element
    min_stack.pop()

    # Current Top element
    print(f'Current Top : {min_stack.top()}')

    # Current Min Element
    print(f'Current Minimum : {min_stack.getMin()}')