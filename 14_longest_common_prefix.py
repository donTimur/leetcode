def longestCommonPrefix(strs: [str]) -> str:
    if not strs:
        return ''

    shortest = min(strs)
    longest = max(strs)
    index = 0

    for i in range(min(len(shortest), len(longest))):
        if shortest[i] != longest[i]:
            break
        else:
            index += 1
    return shortest[:index]

#Input: strs = ["flower","flow","flight"]
#Output: "fl"