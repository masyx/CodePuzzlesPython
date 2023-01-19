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

# O(n) time | O(1) space
def find_key(given_dict, given_value):
    for key, value in given_dict.items():
        if value == given_value:
            return key
    return None

def main():
    my_dict = {'key1':"aaa", 'key2': "bbb", 'key3': "aaa"}
    key = find_key(my_dict, "aaa")
    print(key)
    
    keys = [k for k, v in my_dict.items() if v == 'aaa']
    print(keys)
    
    
    
    
if __name__ == "__main__":
    main()