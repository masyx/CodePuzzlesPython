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
    num_of_coins = [float("inf") for x in range(n + 1)]
    num_of_coins[0] = 0
    for denom in denoms:
        for amount in range(n + 1):
            if denom <= amount:
                amount_left = amount - denom
                coins_at_amount_left= num_of_coins[amount_left]
                num_of_coins[amount] = min(num_of_coins[amount], 1 + coins_at_amount_left)
    return num_of_coins[n] if num_of_coins[n] != float("inf") else -1



def main():
    coins = [2, 3]
    change = 5
    print(min_number_of_coins_for_change(change, coins))


if __name__ == "__main__":
    main()
