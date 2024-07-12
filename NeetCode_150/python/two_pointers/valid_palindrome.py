"""
Problem: Valid Palindrome

Difficulty: Easy

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example:
Input: s = "Was it a car or a cat I saw?"

Output: true
"""

def isPalindrome(s: str) -> bool:
    new = ""
    for a in s:
        if a.isalpha() or a.isdigit():
            new += a.lower()
    return new == new[::-1]
