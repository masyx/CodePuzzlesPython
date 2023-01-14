class Solution:
    def remove_even(lst):
        odds = []
        for n in lst:
            if n % 2 != 0:
                odds.append(n)
        return odds
    
    def remove_even_reverse(lst):
        for i in range(len(lst) - 1, -1, -1):
            if lst[i] % 2 == 0:
                del lst[i]
        return lst
    
    def remove_even_comprehension(lst):
        return [x for x in lst if x % 2 != 0]

def main():
    my_list = [value for value in range(1, 11)]
    print(f"Original list: {my_list}")
    print(f"List without even numbers: {Solution.remove_even_comprehension(my_list)}")
    
    
if __name__ == "__main__":
    main()