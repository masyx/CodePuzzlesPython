# O(n) time | O(1) space, as there can be a maximum of three types of fruits in the basket
def fruits_into_baskets(fruits):
    l = 0
    total_fruits = 0
    fruit_types = {}
    for r in range(len(fruits)):
        right_fruit = fruits[r]
        fruit_types[right_fruit] = fruit_types.get(right_fruit, 0) + 1
        while len(fruit_types) > 2:
            left_fruit = fruits[l]
            fruit_types[left_fruit] -= 1
            if fruit_types[left_fruit] == 0:
                del fruit_types[left_fruit]
            l += 1
            
        total_fruits  = max(total_fruits, r - l + 1)
    return total_fruits


def main():
    # ['A', 'C', 'C', 'C', 'C', 'B', 'C', 'W', 'W', 'W', 'W']
    fruits = ['A', 'C', 'C', 'C', 'C', 'B', 'C', 'W', 'W', 'W', 'W']
    print(fruits_into_baskets(fruits))
    
    
if __name__ == "__main__":
    main()