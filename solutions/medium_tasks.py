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





def main():
    sol = Solution()

    print(sol.divide(-2147483648, 1))


if __name__ == '__main__':
    main()
