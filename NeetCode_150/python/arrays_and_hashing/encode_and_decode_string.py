"""
Problem: Encode and Decode Strings

Difficulty: Medium

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.  Implement the encode and decode methods.

Example:
Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

"""

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            n = len(s)
            res += str(n) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        s_list = []
        n = len(s)
        i = 0

        while i < n:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            s_list.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return s_list
