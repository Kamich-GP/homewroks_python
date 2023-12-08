# Given an integer array nums, move all 0's to the end of it while maintaining ' \
# the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in nums:
        if i == 0:
            nums.remove(0)
            nums.append(0)