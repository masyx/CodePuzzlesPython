class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


# O(n^2) time, we left out n*log(n) time
# complexity of sorting function because
# n^2 dwarfs it | O(n) space 
def threeNumberSum(array, targetSum):
    result = []
    array.sort()
    for i in range(len(array)):
        l = i + 1
        r = len(array) - 1
        while l < r:
            current_sum = array[i] + array[l] + array[r]
            if current_sum == targetSum:
                result.append([array[i], array[l], array[r]])
                l += 1
                r -= 1
            elif current_sum < targetSum:
                l += 1
            else:
                r -= 1
    return result

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    seen_numbers = {}
    for number in array:
        possible_number = targetSum - number
        if possible_number in seen_numbers:
            return [possible_number, number]
        seen_numbers[number] = True
    return []

# O(n*log(n)) time | O(1) space
def pair_with_targetsum(arr, target_sum):
    arr.sort()
    l, r = 0, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == target_sum:
            return [l, r]
        elif arr[l] + arr[r] < target_sum:
            l += 1
        else:
            r -= 1
    return [-1, -1]





def main():
    target=11
    array = [2, 5, 9, 11]
    print(threeNumberSum(array, 0))
    
if __name__ == "__main__":
    main()