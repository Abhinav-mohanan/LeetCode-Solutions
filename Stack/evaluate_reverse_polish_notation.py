"""
Problem : Evaluate Reverse Polish Notation
Difficulty : Medium
Link :- https://leetcode.com/problems/evaluate-reverse-polish-notation/

Approach:
- Use a stack to track integers.
- Traverse the list of tokens.
    - If the token is a number, push it onto the stack.
- If the token is an operator (+, -, *, /):
    - Pop the top two numbers from the stack. 
        The first popped number is the second operand (num2), 
        and the second popped number is the first operand (num1).
    - Apply the operator to these two numbers.
    - Truncate division toward zero as required by Python's integer 
      division rules for negative numbers (using int(num1 / num2)).
    - Push the result back onto the stack.
- After processing all tokens, the stack will contain exactly one element, which is the result.

Complexity
- Time  : O(n)
- Space : O(n) 

"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token in operators:

                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
                
        return stack[0]


if __name__ == '__main__':
    sol = Solution()
    
    print(sol.evalRPN(["2", "1", "+", "3", "*"]))
    print(sol.evalRPN(["4","13","5","/","+"]))
    print(sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
