import sys
from typing import List


def permute(self, nums: List[int]) -> List[List[int]]:
    def backtrack(cur_list: List[int], remains: List[int]):
        if len(remains) == 0:
            res.append(cur_list)
        else:
            for idx in range(len(remains)):
                if idx > 0 and remains[idx] == remains[idx - 1]:
                    continue
                copy = remains[:]
                new_list = cur_list[:]
                new_list.append(copy[idx])
                del copy[idx]
                backtrack(new_list, copy)

    res = list()
    backtrack([], sorted(nums))
    return res


def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    def find_min_greater(nums: List[int], value: int, value_pos: int) -> int:
        min_greater, pos = sys.maxsize, None
        for idx in range(value_pos + 1, len(nums)):
            if value < nums[idx] < min_greater:
                min_greater = nums[idx]
                pos = idx
        return pos

    pos = None
    for idx in range(len(nums) - 1, -1, -1):
        pos = find_min_greater(nums, nums[idx], idx)
        if pos:
            buf = nums[idx]
            nums[idx] = nums[pos]
            nums[pos] = buf
            pos = idx
            break

    if pos is not None:
        nums[pos + 1:len(nums)] = sorted(nums[pos + 1:len(nums)])
    else:
        nums.sort()