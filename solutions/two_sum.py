from typing import List


class Solution:
    """
    Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

    Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.
    Example:

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    """
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        l = N - 1
        r = 0

        while r < l:
            if nums[r] + nums[l] == target:
                return [r + 1, l + 1]
            if nums[r] + nums[l] > target:
                l -= 1
            else:
                r += 1


def main():
    n = int(input("List size: "))

    int_list = list()
    for i in range(n):
        int_list.append(int(input()))

    target = int(input("Target value: "))

    res = Solution().two_sum(int_list, target)

    print(res)


if __name__ == "__main__":
    main()
