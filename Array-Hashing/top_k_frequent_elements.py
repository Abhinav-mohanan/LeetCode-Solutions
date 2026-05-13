"""
Problem : Top K Frequent Elements
Difficulty : Medium
Link :- https://leetcode.com/problems/top-k-frequent-elements/

Approach:
- Use a hashmap to count frequencies.
- Sort the hashmap items based on the frequency in descending order.
- Collect the first k frequent elements
- Return the result

Complexity:
- Time: O(n log n)
- Space: O(n)

"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        res = []

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        frequency_map = dict(sorted(frequency_map.items(), key=lambda x: x[1], reverse=True))

        for key in frequency_map.keys():
            res.append(key)
            if len(res) == k:
                return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
    print(sol.topKFrequent([5,3,1,1,1,3,5,73,1], 3))

