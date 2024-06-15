""" 
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum 
of the square of all of its digits, leads us to number 1. All other (not-happy) numbers will never reach 1. 
Instead, they will be stuck in a cycle of numbers which does not include 1.

2^2 + 3 ^2 = 4 + 9 = 13
1^2 + 3^2 = 1 + 9 = 10
1^2 + 0^2 = 1 + 0 = 1 """

# O(1) space
# Running time is really hard to determine, go to educative for 
# detailed explanation 
'''
The time complexity of the algorithm is difficult to determine. However we know the fact that all unhappy numbers 
eventually get stuck in the cycle: 4 -> 16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4
This sequence behavior tells us two things:
1. If the number N is less than or equal to 1000, then we reach the cycle or 1 in at most 1001 steps.
2. For N > 1000, suppose the number has M digits and the next number is N1. From the above Wikipedia 
link(https://en.wikipedia.org/wiki/Happy_number#Specific_%7F'%22%60UNIQ--postMath-00000027-QINU%60%22'%7F-happy_numbers), 
we know that the sum of the squares of the digits of N is at most 9^2M, or 81M (this will happen when all 
digits of N are 9).
This means:
1. N1 < 81M
2. As we know M = log(N+1)
3. Therefore: N1 < 81 * log(N+1)=> N1 = O(logN)
This concludes that the above algorithm will have a time complexity of O(logN).
'''
def find_happy_number(num):
    slow = fast = num
    while True:
        slow = find_sum_of_square_of_all_digits(slow)
        fast = find_sum_of_square_of_all_digits(find_sum_of_square_of_all_digits(fast))
        if slow == fast:
            break
    return slow == 1

def find_sum_of_square_of_all_digits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** 2
        num //= 10
    return sum

def find_happy_number_set(num):
    seen_numbers = set()
    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        num = find_sum_of_square_of_all_digits(num)
    return num == 1

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))
    print()
    print(find_happy_number_set(23))
    print(find_happy_number_set(12))


main()