'''
121. Best Time to Buy and Sell Stock | Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''
from typing import List


def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    lowest = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        curr_price = prices[i]
        if curr_price <= lowest:
            lowest = curr_price
        elif (curr_price - lowest) > profit:
            profit = curr_price - lowest
    return profit

def maxProfitImproved(prices: List[int]):
    if not prices:
        return 0
    
    lowest = prices[0]
    profit = 0
    
    for curr_price in prices[1:]:
        lowest = min(curr_price, lowest)
        profit = max(profit, curr_price - lowest)
        
    return profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))
    print(maxProfitImproved(prices))
