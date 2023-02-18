# O(n) time | O(n) space
def max_min(lst: list):
    start = 0
    end = len(lst) - 1
    result = []
    while start < end:
        result.append(lst[end])
        result.append(lst[start])
        end -= 1
        start += 1
    if len(lst) % 2 == 1:
        result.append(lst[end])
    return result

# O(n) time | O(n) space
def max_min_pythonic(lst):
    result = []
    for i in range(len(lst) // 2):
        result.append(lst[-(i + 1)])
        result.append(lst[i])
    if len(lst) % 2 == 1:
        result.append(lst[len(lst) // 2])
    return result

# O(n) time | O(1) space   DID NOT IMPLEMENT, JUST COPIED
def max_min_tricky(lst):
    if (len(lst) == 0):
        return []

    maxIdx = len(lst) - 1
    minIdx = 0
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst 

def main():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(max_min(lst))
    

if __name__ == "__main__":
    main()