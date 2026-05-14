"""
Problem : Top K Frequent Elements
Difficulty : Medium
Link :- https://leetcode.com/problems/top-k-frequent-elements/

Approach:
- Use a hashmap to count the frequency of each number.
- Create buckets where the index represents the frequency.
- Place numbers into their corresponding frequency bucket.
- Traverse the buckets in reverse order to get the most frequent elements.
- Collect elements until k elements are found.

Complexity:
- Time: O(n)
- Space: O(n)

"""
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        res = []

        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for val, freq in frequency_map.items():
            bucket[freq].append(val)
        
        for freq in range(len(bucket) - 1, -1, -1):
            for num in bucket[freq]:
                res.append(num)

                if len(res) == k:
                    return res
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
    print(sol.topKFrequent([5,3,1,1,1,3,5,73,1], 3))
