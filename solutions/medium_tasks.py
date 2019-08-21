import sys
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(curr_sum: int, cur_list:  List[int], main_list:  List[int]) -> None:
            for i in range(len(main_list)):
                if curr_sum + main_list[i] == target:
                    solution.append(cur_list + [main_list[i]])
                    return
                if curr_sum + main_list[i] > target:
                    return
                else:
                    backtrack(curr_sum + main_list[i], cur_list + [main_list[i]], main_list[i:])

        solution = []
        backtrack(0, [], sorted(candidates))

        return solution

    def letterCombinations(self, digits: str) -> List[str]:

        digits_dict = {
            "1": {},
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def _letterCombinations(digits: str) -> List[str]:
            if len(digits) == 0:
                return []
            possible_digits = digits_dict.get(digits[0])
            if len(digits) == 1:
                return possible_digits
            else:
                res = []
                for idx in range(len(possible_digits)):
                    res += [possible_digits[idx] + comb for comb in _letterCombinations(digits[1:])]
            return res

        return _letterCombinations(digits)

    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(sequence: str, n: int, left_count: int, right_count: int, solution: List[str]):
            if right_count > left_count:
                return
            if n == 0:
                if right_count == left_count:
                    solution.append(sequence)
            else:
                backtrack(sequence + "(", n - 1, left_count + 1, right_count, solution)
                backtrack(sequence + ")", n - 1, left_count, right_count + 1, solution)

        solution = []
        backtrack("", n * 2, 0, 0, solution)
        return solution

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
            nums[pos + 1:len(nums)] = sorted(nums[pos+1:len(nums)])
        else:
            nums.sort()





def main():
    sol = Solution()

    print(sol.divide(-2147483648, 1))


if __name__ == '__main__':
    main()
