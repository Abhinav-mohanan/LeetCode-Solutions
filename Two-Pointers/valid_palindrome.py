"""
Problem : Valid Palindrome
Difficulty : Easy
Link :- https://leetcode.com/problems/valid-palindrome/

Approach:
- Initialize:
    - 'left' pointer at the beginning of the string.
    - 'right' pointer at the end of the string.
- Move both pointers toward the center.
- Ignore non-alphanumeric characters using 'isalnum()'.
- Compare characters after converting them to lowercase.
    - If characters are different, return False.
    - Otherwise, continue checking.
- If all characters match, return True.

Complexity
- Time  : O(n)
- space : O(1)

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == '__main__':
    sol = Solution()
    
    # Test cases
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))  
    print(sol.isPalindrome("race a car"))                      
    print(sol.isPalindrome(" "))