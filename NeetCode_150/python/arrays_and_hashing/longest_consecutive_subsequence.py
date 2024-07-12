"""
Problem: Longest Consecutive Subsequence

Difficulty: Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [2,20,4,10,3,4,5]

Output: 4
"""

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for n in nums:
        if n - 1 not in num_set:
            length = 0
            while (n + length) in num_set:
                length += 1
            longest = max(longest, length)
    return longest
