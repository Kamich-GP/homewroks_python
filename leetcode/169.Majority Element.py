# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

def number(nums):
    for a in nums:
        for b in nums:
            if nums.count(a) > nums.count(b) and b != a:
                return a
            elif nums.count(b) > nums.count(a) and b != a:
                return b
nums = [2,2,1,1,1,2,2]
print(number(nums))