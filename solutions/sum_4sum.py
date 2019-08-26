from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum == target:
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        l += 1
        return [list(t) for t in result]


def main():
    solution = Solution()
    nums = [-1, -5, -5, -3, 2, 5, 0, 4]
    print(solution.fourSum(nums, 0))


if __name__ == "__main__":
    main()
