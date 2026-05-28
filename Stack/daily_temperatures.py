"""
Problem : Daily Temperatures
Difficulty : Medium
Link :- https://leetcode.com/problems/daily-temperatures/

Approach:
- Use a stack to store indexes of temperatures that are still waiting
    for a warmer future temperature.
- Traverse the array from left to right 
- while comparing the current
    temperature with the temperatures stored in the stack.
- If the current temperature is warmer:
    - Remove the previous index from the stack.
    - Calculate how many days it took to find a warmer temperature.
    - Keep removing elements until the stack becomes empty
        or the current temperature is no longer warmer.
- Push the current index into the stack for future comparisons.

Complexity
- Time : O(n)
- Space : O(n)

"""
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temp:
                
                previous_day = stack.pop()
                answer[previous_day] = i - previous_day
            
            stack.append(i)
        
        return answer

if __name__ == "__main__":
    
    sol = Solution()

    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(sol.dailyTemperatures([30,40,50,60]))
    print(sol.dailyTemperatures([30,60,90]))
