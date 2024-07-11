"""
Problem: Group Anagrams
Difficulty: Medium

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

Example:
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

"""

from typing import List
from collections import defaultdict

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    group_anagrams = defaultdict(list)

    for s in strs:
        s_chars = [0]*26
        for c in s:
            s_chars[ord(c) - ord('a')] += 1
        group_anagrams[tuple(s_chars)].append(s)
    
    return group_anagrams.values()