nums = [1, 0, 1, 0, 1]
goal = 2
c = 0
subarrays = []
n = len(nums)

for start in range(n):
    for end in range(start, n):
        subarray = nums[start:end + 1]
        subarrays.append(subarray)

for i in subarrays:
    if sum(i) == goal:
        c += 1

print(c)

