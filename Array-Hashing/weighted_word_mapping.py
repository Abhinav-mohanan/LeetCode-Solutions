"""
Problem : Weighted Word Mapping
Difficulty : Easy
Link :- https://leetcode.com/problems/weighted-word-mapping/

Approach:
- Each character has a weight given in the weights array.
- For every word:
    - Calculate the total weight of the word.
    - For each character:
        - Find its index using:
            ord(char) - ord('a')
        - Add the corresponding weight.
- Take the total weight modulo 26.
- Convert the result into a character.
- The mapping formula is:
    chr(ord('z') - modulo)
- Append the mapped character to the result.
- Return the final string.

Complexity
- Time  : O(n * m)
- Space : O(n * m)

"""
class Solution:
    def mapWords(self, words: list[str], weights: list[int]) -> str:

        result = []

        for word in words:

            weight = 0

            for char in word:
                index = ord(char) - ord('a')
                weight += weights[index]

            modulo = weight % 26
            mapped_char = chr(ord('z') - modulo)

            result.append(mapped_char)

        return "".join(result)


if __name__ == "__main__":

    solution = Solution()

    print(solution.mapWords(
        ["abcd", "def", "xyz"],
        [5, 3, 12, 14, 1, 2, 3, 2, 10, 6, 6, 9, 7, 8, 7, 10, 8, 9, 6, 9, 9, 8, 3, 7, 7, 2]))
    
    print(solution.mapWords(
        ["a", "b", "c"],
        [1] * 26))
