"""
Problem: Duplicate Integer

Difficulty: Easy

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example:
Input: nums = [1, 2, 3, 3]

Output: true

"""

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    num_set = set()

    for n in nums:
        if n not in num_set:
            num_set.add(n)
        else:
            return True
    return False