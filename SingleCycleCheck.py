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



def main():

    arr = [2, 3, 1, -4, -4, 2]
    print(hasSingleCycleMy(arr))
    
if __name__ == "__main__":
    main()