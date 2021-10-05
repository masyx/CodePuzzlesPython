
while True:
    try:
        change = 100 * float(input("Change: "))
        if change < 0: raise ValueError
        break;
    except ValueError:
        print("This is not a number, pleae enter valid number") 

coins = [25, 10, 5, 1]

totalCoinsCount = 0

for coin in coins:
    coinsCount = 0
    coinsCount = int(change / coin)
    change = change % coin
    totalCoinsCount += coinsCount
    if change == 0:
        break;

print(f"Total amount of coins is: {totalCoinsCount}")