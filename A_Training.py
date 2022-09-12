# O()
def search_triplets(arr):
    triplets = []
    arr.sort()
    for i in range(len(arr)):
        l = i + 1
        r = len(arr) - 1
        while l < r:
            curr_sum = arr[i] + arr[l] + arr[r]
            if curr_sum == 0:
                triplets.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1
            elif curr_sum > 0:
                r -= 1
            else:
                l += 1
    return triplets



def main():
    array = [-2, -1, 0, 2, 3]
    print(search_triplets(array))
    
if __name__ == "__main__":
    main()