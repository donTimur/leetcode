#https://leetcode.com/problems/roman-to-integer/

def romanToInt(s: str) -> int:
    result, previous = 0, 0
    map_roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in s[::-1]:
        if map_roman_to_int[i] >= previous:
            result += map_roman_to_int[i]
        else:
            result -= map_roman_to_int[i]

        previous = map_roman_to_int[i]

    return result
