import functools
import sys

print("qwerty"[1:])

print(int("01"))

print(sys.maxsize)

nums = [1, 1, 2]
for idx in range(len(nums) - 1, -1, -1):
    print(idx)

nums = [1, 3, 2]
nums[1:2] = sorted(nums[1:2])
print(nums)
print(nums[1:2])

for i in reversed(range(10)):
    print(i)

print(-2147483648)

result = -2147483648
print(result < -2**31)

res = []
ar = [[-1, 1, 2], [0, 0, 2]]
res.extend([[-2] + v for v in ar])
print(res)

ar = [1, 2, 3, 4, 5]

print(list(filter(
    lambda x: x % 2 == 0,
    map(lambda x: x * 10, ar)
)))

print(functools.reduce((lambda x, y: x + y), ar))


ar = [1, 3, 5, 7, 9]
print(list(zip(ar)))

print(ar[-1])

for j in range(2, 3):
    print(j)


nums = list(range(1, 10))
print(nums)

for i in range(10, 11):
    print(i)