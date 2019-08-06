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



def main():
    nums = []
    print(Solution().threeSum(nums))


if __name__ == "__main__":
    main()
