def maxProfit(prices) -> int:
    lowest = prices[0]
    profit = 0
    for price in prices:
        lowest = min(lowest, price)
        profit = max(price - lowest, profit)
    return profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4, 0, 10]
    print(maxProfit(prices))