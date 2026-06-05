"""
Problem : Count Digit Appearances
Difficulty : Medium
Link :- https://leetcode.com/problems/count-digit-appearances/

Approach:
- We need to count how many times the given digit appears in all numbers of the array.
- Traverse each number in nums one by one.
- For every number:
    - Extract its digits using modulo (% 10).
    - Compare each digit with the target digit.
    - If they are equal, increment the answer.
- Remove the last digit using integer division (// 10).
- Continue until all digits of the current number are processed.
- Return the total count after processing all numbers.


Complexity
- Time  : O(n * d)
- Space : O(1)

  n = number of elements in nums
  d = number of digits in each number

"""

class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:

        total_count = 0

        for num in nums:
            
            current = num

            while current:

                current_digit = current % 10

                if current_digit == digit:
                    total_count += 1
                
                current //= 10
            
        return total_count
    
if __name__ == "__main__":

    sol = Solution()

    print(sol.countDigitOccurrences([12,54,32,22], 2))
    print(sol.countDigitOccurrences([1,34,7], 9))


# Note:

# A concise Python solution is:
#  return str(nums).count(str(digit))
# Convert the list to a string and count the occurrences of the target digit.