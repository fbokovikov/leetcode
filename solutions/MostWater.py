from typing import List


class Solution:
    @staticmethod
    def maxArea(height: List[int]) -> int:
        max_area = 0

        l = 0
        r = len(height) - 1

        while l < r:
            max_area = max(max_area, (r - l) * min(height[r], height[l]))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return max_area


def main():
    res = Solution.maxArea([1, 5, 4, 3])
    print("Max area:", res)


if __name__ == "__main__":
    main()
