# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.
def findDisappearedNumbers(nums):
    maximal = len(nums) + 1
    list = []
    for i in range(1, maximal):
        if i not in nums:
            list.append(i)
    return list
# на 30 кейсе даёт ошибку по времени из-за слишком огромного списка с цифрами. Но сам код точно подходит для решения
