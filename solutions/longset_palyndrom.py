class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length, length = 0, len(s)
        start_pos, end_pos = 0, 0
        for cur_pos in range(length):
            len1 = self.expandAroundCenter(s, cur_pos, cur_pos)
            len2 = self.expandAroundCenter(s, cur_pos, cur_pos + 1)
            cur_length = max(len1, len2)
            if cur_length > max_length:
                max_length = cur_length
                start_pos = cur_pos - (cur_length - 1) // 2
                end_pos = cur_pos + cur_length // 2

        return s[start_pos:end_pos + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        length, res = len(s), 0
        res = 0
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
            res += 1
        return right - left - 1


def main():
    s = input("Input string: ")
    solution = Solution()
    palindrome = solution.longestPalindrome(s)
    print("longest palindrome:", palindrome)


if __name__ == '__main__':
    main()
