def maxProfit(prices) -> int:
    if not prices:
        return 0
    smallest = prices[0]
    max_profit = 0
    for price in prices[1:]:
        max_profit = max(max_profit, price - smallest)
        smallest = min(smallest, price)
    return max_profit


def maxProfit_2(prices):
    if not prices:
        return 0
    smallest = prices[0]
    max_profit = 0
    for price in prices[1:]:
        current_profit = price - smallest
        if current_profit > max_profit:
            max_profit = current_profit
        if price < smallest:
            smallest = price
    return max_profit

if __name__ == "__main__":
    prices = [1]
    print(maxProfit_2(prices))