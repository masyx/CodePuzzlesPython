# O(n*log(n)) time | O(n) space, where n is the length of the array
def minHeightBst(array):
    return construct_bst(array, None, 0, len(array) - 1)


def construct_bst(array, bst, left_idx, right_idx):
    if left_idx > right_idx:
        return None
    mean_idx = (left_idx + right_idx) // 2
    if bst is None:
        bst = BST(array[mean_idx])
    else:
        bst.insert(array[mean_idx])
    construct_bst(array, bst, left_idx, mean_idx - 1)
    construct_bst(array, bst, mean_idx + 1, right_idx)
    return bst

def find_closest_int_to_mean(array, mean):
    closest_to_mean_idx = 0
    original_diff = abs(mean - array[0])
    for i in range(1, len(array)):
        curr_difference = abs(mean - array[i])
        if curr_difference < original_diff:
            closest_to_mean_idx = i
            original_diff = curr_difference
    return closest_to_mean_idx


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
                
                
def main():
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    bst = minHeightBst(array)
    print(bst)
    
    
if __name__ == "__main__":
    main()