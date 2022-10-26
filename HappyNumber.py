""" 
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum 
of the square of all of its digits, leads us to number 1. All other (not-happy) numbers will never reach 1. 
Instead, they will be stuck in a cycle of numbers which does not include 1.

2^2 + 3 ^2 = 4 + 9 = 13
1^2 + 3^2 = 1 + 9 = 10
1^2 + 0^2 = 1 + 0 = 1 """

def find_happy_number(num):
    # TODO: Write your code here
    return False


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()