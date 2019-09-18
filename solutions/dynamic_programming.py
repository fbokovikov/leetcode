from typing import List


class Solution:
    def maxSubArray(nums: List[int]) -> int:
        max_sum, cur_sum = nums[0], 0
        for num in nums:
            cur_sum += num
            max_sum = max(cur_sum, max_sum)
            cur_sum = max(cur_sum, 0)
        return max_sum

    def climbStairs(self, n: int) -> int:
        steps = [None] * (n + 2)
        steps[1] = 1
        steps[2] = 2
        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[n]

    def rob(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        max_robs = [0] * n
        max_robs[0] = nums[0]
        max_robs[1] = max(nums[0], nums[1])
        for i in range(2, n):
            max_robs[i] = max(nums[i] + max_robs[i - 2], max_robs[i - 1])
        return max_robs[n - 1]

    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        res = 0
        for price in prices:
            cur_min = min(price, cur_min)
            res = max(res, price - cur_min)
        return res


def main():
    sol = Solution()
    print(sol.climbStairs(1))


if __name__ == '__main__':
    main()
