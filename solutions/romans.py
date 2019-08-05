I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

"""
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:

    @staticmethod
    def romanToInt(s: str) -> int:
        roman_to_decimals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum = 0
        for index in range(len(s)):
            sum += roman_to_decimals[s[index]]
            if index == 0:
                continue
            if roman_to_decimals[s[index - 1]] < roman_to_decimals[s[index]]:
                sum -= 2 * roman_to_decimals[s[index - 1]]

        return sum

    @staticmethod
    def intToRoman(num: int) -> str:
        romans = {
            1: {1: "I", 4: "IV", 5: "V", 9: "IX"},
            10: {1: "X", 4: "XL", 5: "L", 9: "XC"},
            100: {1: "C", 4: "CD", 5: "D", 9: "CM"},
            1000: {1: "M"}
        }
        key, res = 1, ""
        while num > 0:
            num, digit = divmod(num, 10)
            if digit == 4:
                res = romans[key][4] + res
            elif digit == 9:
                res = romans[key][9] + res
            else:
                res = (romans[key][1] * digit if digit < 5 else romans[key][5] + romans[key][1] * (digit - 5)) + res
            key = key * 10
        return res


def main():
    """main"""

    """
    s = input("Input string: ")
    int_value = Solution.romanToInt(s)
    print("Int value:", int_value)
    """

    val = int(input("Input num: "))
    roman_value = Solution.intToRoman(val)
    print("Roman value:", roman_value)


if __name__ == "__main__":
    main()
