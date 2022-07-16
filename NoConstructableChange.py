from operator import contains
from typing import List


def main():
    coins = [1, 1, 1,1,1]#[5, 7, 1, 1, 2, 3, 22] # [1, 1, 2, 3, 5, 7, 22]
    print(nonConstructibleChange(coins))

def nonConstructibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin
            
    return change + 1
    
    
    


if __name__ == "__main__":
    main()