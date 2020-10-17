#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums: [int]) -> int:
    index = 1

    while index < len(nums):
        if nums[index] == nums[index - 1]:
            nums.pop(index)
        else:
            index += 1
    return index
