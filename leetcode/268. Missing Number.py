# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
def missingNumber(nums):
    maximal = max(nums)
    for i in range(0,maximal):
        if i not in nums:
            return i
print(missingNumber([5, 4, 3, 1, 0]))