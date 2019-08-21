import sys
from typing import List, Tuple


class Solution:
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

    :param nums: int list

    :return: triplets such as a + b + c = 0
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        result, cur_value = [], nums[-1]
        if nums.count(0) >= 3:
            result.append([0, 0, 0])
        for idx in range(len(nums)):
            if cur_value == nums[idx]:
                continue
            if nums[idx] >= 0:
                return result
            found_tuples = self._twoSum(nums, -nums[idx], idx)
            for tup in found_tuples:
                result.append([nums[idx], tup[0], tup[1]])
            cur_value = nums[idx]
        return result

    def _twoSum(self, nums: List[int], target: int, idx: int) -> List[Tuple]:
        res = set()
        l = idx + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                pair = (nums[l], nums[r])
                res.add(pair)
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return res

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        closest_sum = None
        cur_diff, min_diff = None, sys.maxsize
        for idx in range(len(nums) - 2):
            cur_closest_sum = self.twoSumClosest(nums, target - nums[idx], idx) + nums[idx]
            cur_diff = abs(target - cur_closest_sum)
            if cur_diff < min_diff:
                min_diff = cur_diff
                closest_sum = cur_closest_sum

        return closest_sum

    def twoSumClosest(self, nums: List[int], target: int, idx: int) -> int:
        l = idx + 1
        r = len(nums) - 1
        closest_sum = sys.maxsize
        sum = nums[l] + nums[r]
        while l < r:
            diff = abs(nums[l] + nums[r] - target)
            if diff < closest_sum:
                closest_sum = diff
                sum = nums[l] + nums[r]
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
        return sum


def main():
    nums = [0,-4,1,-5]
    print(Solution().threeSumClosest(nums, 0))


if __name__ == "__main__":
    main()
