def sum_two(nums, target):
    for a in range(0, len(nums)):
        for b in range(0, len(nums)):
            if nums[a] + nums[b] == target and a != b:
                return [a, b]

nums = [3, 3]
target = 6
print(sum_two(nums, target))
