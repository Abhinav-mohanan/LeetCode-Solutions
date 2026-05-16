"""
Problem: Longest Consecutive Sequence
Difficulty: Medium
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Approach:
- Convert the array into a set for O(1) lookup and remove duplicates.
- Iterate through each number in the set
- A number starts a sequence only if (num - 1) is not 
   present in the set
- Find the length of the consecutive sequence using a while loop.
- Update the longest sequence length

Complexity:
- Time: O(n)
- Space: O(n)

"""


from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            
            # Start counting only from the beginning of a sequence
            if num - 1 not in nums_set:

                length = 0 

                while num + length in nums_set:
                    length += 1
                
                longest = max(longest, length)

        return longest

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

                
    