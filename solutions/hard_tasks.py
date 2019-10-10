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

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        position = 0
        while position < len(intervals):
            if intervals[position][0] > newInterval[0]:
                break
            position += 1
        intervals.insert(position, newInterval)
        res = []
        cur_interval = intervals[0]
        for interval in intervals:
            if interval[0] <= cur_interval[1]:
                cur_interval[1] = max(cur_interval[1], interval[1])
            else:
                res.append(cur_interval)
                cur_interval = interval
        res.append(cur_interval)
        return res


def main():
    sol = Solution()
    nums2 = [2, 1,0]
    nums3 = [7, 8, 9, 11, 12]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    print(sol.insert(intervals, new_interval))


if __name__ == '__main__':
    main()
