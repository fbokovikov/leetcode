import sys
from typing import List


class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor:
            return 0
        result = 0
        while dividend >= divisor:
            koef, new_divisor = 1, divisor
            while dividend >= new_divisor:
                dividend -= new_divisor
                result += koef
                new_divisor += new_divisor
                koef +=koef
        if not sign:
            result = -result
        if (result >= 2**31) or (result < -2**31):
            return 2**31 - 1
        return result

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)
        for i in reversed(range(n1)):
            for j in reversed(range(n2)):
                idx = i + j;
                total = res[idx + 1] + int(num1[i]) * int(num2[j])
                res[idx + 1] = total % 10
                res[idx] += total // 10
        result = ""
        for digit in res:
            if not result and digit == 0:
                continue
            result += str(digit)
        return result

    def convert(self, s: str, numRows: int) -> str:
        """
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        """
        if numRows == 1:
            return s
        rows = [""] * numRows
        cur_row, direction = 0, 1
        for letter in s:
            rows[cur_row] += letter
            cur_row += direction
            if (cur_row == numRows - 1) or (cur_row == 0):
                direction = -direction
        return "".join(rows)

    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31
        res, sign = 0, True
        sign_visited = False
        digit_visited = False
        for letter in s:
            if letter == ' ':
                if sign_visited or digit_visited:
                    break
                continue
            if letter == '-':
                if sign_visited or digit_visited:
                    break
                sign_visited = True
                sign = False
            elif letter == '+':
                if sign_visited or digit_visited:
                    break
                sign_visited = True
            elif not ('0' <= letter <= '9'):
                break
            else:
                digit_visited = True
                res = res * 10 + int(letter)
                if res > MAX_INT:
                    return MAX_INT if sign else MIN_INT
        res = res if sign else -res
        return res

    def search(self, nums: List[int], target: int) -> int:
        """
        [4, 5, 6, 7, 0, 1, 2] - log n
        """
        if nums is None or len(nums) == 0:
            return -1
        length = len(nums) - 1
        rotation_idx = self.binary_search_rotation(nums, 0, length)
        if nums[rotation_idx + 1] <= target <= nums[length]:
            return self.binary_search(nums, target, rotation_idx + 1, length)
        else:
            return self.binary_search(nums, target, 0, rotation_idx)

    def binary_search_rotation(self, nums: List[int], start, end):
        if start == end:
            return -1
        while start <= end:
            mid = (start + end) // 2
            if mid == end:
                break
            if nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        return -1

    def binary_search(self, nums: List[int], target: int, start, end):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_pos = self.binary_search_first(nums, target, 0, len(nums) - 1)
        if first_pos == -1:
            return [-1, -1]
        end_pos = self.binary_search_last(nums, target, first_pos, len(nums) - 1)
        return [first_pos, end_pos]

    def binary_search_last(self, nums, target, start_pos, end_pos):
        while start_pos <= end_pos:
            middle = (start_pos + end_pos) // 2
            if nums[middle] == target and (middle == end_pos or nums[middle + 1] > target):
                return middle
            elif nums[middle] > target:
                end_pos = middle - 1
            else:
                start_pos = middle + 1
        return - 1

    def binary_search_first(self, nums, target, start_pos, end_pos):
        while start_pos <= end_pos:
            middle = (start_pos + end_pos) // 2
            if nums[middle] == target and (middle == start_pos or nums[middle - 1] < target):
                return middle
            elif nums[middle] >= target:
                end_pos = middle - 1
            else:
                start_pos = middle + 1
        return -1

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        N = n - 1
        for i in range(n // 2):
            for j in range(n - 2 * i - 1):
                buf = matrix[i][i + j]
                matrix[i][i + j] = matrix[N - i - j][i]
                matrix[N - i - j][i] = matrix[N - i][N - i - j]
                matrix[N - i][N - i - j] = matrix[i + j][N - i]
                matrix[i + j][N - i] = buf








def main():
    sol = Solution()
    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    sol.rotate(matrix)
    for row in matrix:
        print(row)


if __name__ == '__main__':
    main()
