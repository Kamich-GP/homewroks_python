# Given an integer array nums,
# return true if any value appears at least twice in the array, and return false if every element is distinct.
def containsDuplicate(nums):
    for i in nums:
        if nums.count(i) > 1:
            return True
        else:
            return False
nums = [1,2,3,1]
print(containsDuplicate(nums))