from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res, index = "", 0
        while True:
            if len(strs[0]) == index:
                return res
            else:
                cur_char = strs[0][index]
            for str in strs:
                if len(str) == index or str[index] != cur_char:
                    return res
            res += cur_char
            index += 1
        return res

    def isValid(self, s: str) -> bool:
        if not str:
            return False
        opening_pairs = {"{": "}", "[": "]", "(": ")"}
        bracket_stack = []
        for bracket in s:
            if bracket in opening_pairs:
                bracket_stack.append(bracket)
            else:
                if not bracket_stack:
                    return False
                if opening_pairs[bracket_stack.pop()] != bracket:
                    return False
        if bracket_stack:
            return False
        return True

    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        start_pos = 0
        while start_pos < len(nums):
            cur_pos = start_pos
            while cur_pos < len(nums) - 1 and nums[cur_pos] == nums[cur_pos + 1]:
                cur_pos += 1
            if cur_pos - start_pos > 0:
                del nums[start_pos:cur_pos]
            start_pos += 1

        return len(nums)

    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None:
            return 0

        idx = 0
        while idx < len(nums):
            if nums[idx] == val:
                del nums[idx]
            else:
                idx += 1
        return len(nums)

    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None or len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        for idx in range(len(haystack) - len(needle) + 1):
            for pos in range(len(needle)):
                if haystack[idx + pos] != needle[pos]:
                    break
                if pos == len(needle) - 1:
                    return idx
        return -1

    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target > nums[-1]:
            return length;
        for idx in range(length):
            if nums[idx] >= target:
                return idx

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n - 1)
            cur_digit, cur_count = prev[0], 0
            res = ""
            for idx in range(len(prev)):
                if prev[idx] == cur_digit:
                    cur_count += 1
                else:
                    res += str(cur_count) + str(cur_digit)
                    cur_count = 1
                    cur_digit = prev[idx]
            res += str(cur_count) + str(cur_digit)
            return res


def main():
    print(Solution().rob([0]))

if __name__ == "__main__":
    main()
