def min_number_of_coins_for_change_greedy(n, denoms):
    num_of_coins = 0
    for denom in reversed(denoms):
        num_of_coins += n // denom
        n = n % denom
        if n == 0:
            return num_of_coins
    return -1

# O(nd) time, where n is target amount and d is number of denominations that we have
# O(n) space
def min_number_of_coins_for_change(n, denoms):
    num_of_coins = [float('inf')] * (n + 1)
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(len(num_of_coins)):
            if denom <= amount:
                left = amount - denom
                total_coins = 1 + num_of_coins[left]
                num_of_coins[amount] = min(num_of_coins[amount], total_coins)
    return num_of_coins[n] if num_of_coins[n] != float('inf') else -1

def main():
    coins = [1, 3, 4]
    change = 10
    print(min_number_of_coins_for_change(change, coins))


if __name__ == "__main__":
    main()
