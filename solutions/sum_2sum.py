from typing import List


def twoSumMap(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff not in nums_map:
            nums_map[nums[i]] = i
        else:
            return [nums_map[diff], i]


def twoSumTwoPointers(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    r = 0
    l = len(nums) - 1
    while r < l:
        if nums[r] + nums[l] == target:
            return [nums[r], nums[l]]
        elif nums[r] + nums[l] < target:
            r += 1
        else:
            l -= 1
    return None
