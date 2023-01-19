# O(n) time | O(n) space
def find_sum_best(lst, sum):
    seen = set()
    for number in lst:
        possible_number = sum - number
        if possible_number in seen:
            return [number, possible_number]
        seen.add(number)
    return []

# O(n log(n)) time | O(1) space
def find_sum(lst: list, sum):
    lst.sort()
    l = 0
    r = len(lst) - 1
    while l < r:
        current_sum = lst[l] + lst[r]
        if current_sum == sum:
            return [lst[l], lst[r]]
        if current_sum > sum:
            r -= 1
        else:
            l += 1
    return []

def main():
    lst = [1,21,3,14,5,60,7,6]
    k = 81
    print(find_sum_best(lst, k))
    
    
    
if __name__ == "__main__":
    main()