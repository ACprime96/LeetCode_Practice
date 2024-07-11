"""
Problem: Top k Frequent Elements

Difficulty: Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example:
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

"""

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    n_freq = {}
    bucket = [[] for i in range(len(nums) + 1)]

    for n in nums:
        n_freq[n] = 1 + n_freq.get(n, 0)
    for n, c in n_freq.items():
        bucket[c].append(n)

    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for n in bucket[i]:
            res.append(n)
            if len(res) == k:
                return res
