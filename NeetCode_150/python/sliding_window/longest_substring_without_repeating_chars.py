"""
Problem: Longest Substring Without Repeating Characters

Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.
A substring is a contiguous sequence of characters within a string.

Example: 
Input: s = "zxyzxyz"

Output: 3

"""

def lengthOfLongestSubstring(s: str) -> int:
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res