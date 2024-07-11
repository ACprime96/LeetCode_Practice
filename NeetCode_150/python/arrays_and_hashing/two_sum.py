"""
Problem: Two Sum

Difficulty: Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    nmap = {}
        
    for i, n in enumerate(nums):
        diff = target - n
        if diff in nmap.keys():
            return [nmap[diff], i]
        nmap[n] = i

    return list()