"""
Problem : Find the Highest Altitude
Difficulty : Easy
Link :- https://leetcode.com/problems/find-the-highest-altitude/

Approach:
- Start at altitude 0.
- Traverse the gain array and keep updating the current altitude.
- After each update, compare it with the highest altitude.
- Store the maximum altitude during the traversal.
- Return the highest altitude.

Complexity
- Time  : O(n)
- Space : O(1)

"""

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        highest_altitude = 0
        current_altitude = 0

        for altitude_gain in gain:

            current_altitude += altitude_gain

            highest_altitude = max(highest_altitude, 
                                   current_altitude)
        
        return highest_altitude
            


if __name__ == "__main__":

    sol = Solution()

    print(sol.largestAltitude([-5,1,5,0,-7]))
    print(sol.largestAltitude([-4,-3,-2,-1,4,3,2]))