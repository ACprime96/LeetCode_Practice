"""
Problem: Valid Anagram

Difficulty: Easy

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Example:
Input: s = "racecar", t = "carrace"

Output: true

"""

def isAnagram(s: str, t: str) -> bool:
    s_letters = [0]*26
    t_letters = [0]*26

    for c in s:
        index = ord(c) - ord('a')
        s_letters[index] += 1
    
    for c in t:
        index = ord(c) - ord('a')
        t_letters[index] += 1
    
    for i in range(26):
        if s_letters[i] != t_letters[i]:
            return False
    
    return True