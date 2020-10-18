#https://leetcode.com/problems/implement-strstr/

def strStr(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    if needle not in haystack:
        return -1

    appearances = haystack.split(needle)

    return len(appearances[0])
