#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums: [int]) -> int:
    index = 1

    while index < len(nums):
        if nums[index] == nums[index - 1]:
            nums.pop(index)
        else:
            index += 1
    return index


#nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
#    return length = 5,
#   with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.