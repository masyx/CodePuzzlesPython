# O(n) time | O(m) space
def rearrange_1(lst: list):
    negative_list = []
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] < 0:
            negative_list.append(lst.pop(i))
    negative_list.reverse()
    return negative_list + lst

# O(n) time | O(1) space
def rearrange(lst: list):
    leftMostEle = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[leftMostEle], lst[i] = lst[i], lst[leftMostEle]
            leftMostEle += 1
    return lst

def rearrange_pythonic(lst):
    return [i for i in lst if i < 0] + [i for i in lst if i >= 0]


def main():
    arr = [-2,-1,20,4,5,-9,-6]
    
    print(rearrange_pythonic(arr))
    
    
if __name__ == "__main__":
    main()