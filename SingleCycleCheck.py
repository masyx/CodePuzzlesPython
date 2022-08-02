# It passed all Algo tests, but I doubt it will hold thousands of tests
# O(n) time | O(n) space
def hasSingleCycleMy(array):
    cyclic = False
    idx = 0
    visited = {idx}
    for i in range(len(array)):
        idx = (idx + array[idx]) % len(array)
        if i == len(array) - 1 and idx != 0:
            return False
        visited.add(idx)
    if len(array) == len(visited):
        cyclic = True
    return cyclic

# O(n) time | O(1) space
def hasSingleCycle(array):
    num_of_visited_elements = 1
    current_idx = 0
    while num_of_visited_elements <= len(array):
        if num_of_visited_elements > 1 and current_idx == 0:
            return False
        # In Python, however, "the modulo operator always yields a result 
        #       with the same sign as its second operand (or zero)"
        # More specifically, the modulo operator in Python behaves as follows when used with a negative first operand:
        #       -x % y == -(x % y) + y
        current_idx = (current_idx + array[current_idx]) % len(array)
        num_of_visited_elements += 1
    return current_idx == 0
    



def main():

    arr = [1,1,-3,-3]
    print(hasSingleCycle(arr))
    
if __name__ == "__main__":
    main()