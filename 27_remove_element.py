#https://leetcode.com/problems/remove-element/

# valid solution but leetcode requires list modification
'''def removeElement(nums: [int], val: int) -> int:
    if val not in nums:
        return len(nums)

    indexes = [i for i, num in enumerate(nums) if num == val]

    return len(nums) - len(indexes)
'''


def removeElement(nums: [int], val: int):
    if val not in nums:
        return len(nums)

    index = 0

    while index < len(nums):
        if nums[index] == val:
            del nums[index]
        else:
            index += 1

    return len(nums)
