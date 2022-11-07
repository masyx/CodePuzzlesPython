def nonConstructibleChange(coins):
    coins.sort()
    minimum_change = 0
    for coin in coins:
        if coin > minimum_change + 1:
            break
        minimum_change += coin
    return minimum_change + 1

def main():
    # 1 1 2 3 5 7 22
    coins = [5, 7, 1, 1, 2, 3, 22]
    print(nonConstructibleChange(coins))


if __name__ == "__main__":
    main()