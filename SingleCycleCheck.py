# left it here for tracking purpose
def hasSingleCycleWrong(array):
    cyclic = False
    idx = 0
    visited = {idx}
    for i in range(len(array) - 1):
        idx = (idx + array[idx]) % len(array)        
        visited.add(idx)
    if len(array) == len(visited):
        cyclic = True
    return cyclic



def main():

    arr = [1, 1, 1, 1, 2]
    print(hasSingleCycle(arr))
    
if __name__ == "__main__":
    main()