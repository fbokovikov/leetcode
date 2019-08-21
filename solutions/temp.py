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
