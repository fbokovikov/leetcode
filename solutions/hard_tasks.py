from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        last_positive_index = self.segregate(nums)
        for idx in range(0, last_positive_index):
            val = abs(nums[idx])
            if val <= last_positive_index and nums[val - 1] > 0:
                nums[val - 1] = -nums[val - 1]
        for i in range(0, last_positive_index):
            if nums[i] > 0:
                return i + 1
        return last_positive_index + 1

    def segregate(self, nums):
        i, j = 0, 0
        while i < len(nums):
            if nums[i] > 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
            i += 1
        return j


def main():
    sol = Solution()
    nums2 = [2, 1,0]
    nums3 = [7, 8, 9, 11, 12]
    print(sol.firstMissingPositive(nums2))
    print(sol.firstMissingPositive(nums3))


if __name__ == '__main__':
    main()
