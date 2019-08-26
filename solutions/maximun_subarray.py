from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sum, cur_sum = nums[0], 0
    for num in nums:
        cur_sum += num
        max_sum = max(cur_sum, max_sum)
        cur_sum = max(cur_sum, 0)
    return max_sum


def main():
    nums = [-5, -1, 0, 2]
    print(maxSubArray(nums))

if __name__ == '__main__':
    main()