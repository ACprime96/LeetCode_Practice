"""
Problem : Best Time to Buy and Sell Stock

Difficulty: Easy

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example:
Input: prices = [10,1,5,6,7,1]

Output: 6
"""
from typing import List

def maxProfit(prices: List[int]) -> int:
    res = 0
        
    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)
    return res