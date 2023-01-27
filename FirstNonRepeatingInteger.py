def find_first_unique(lst):
    for i in range(len(lst)):
        j = i + 1
        while j < len(lst):
            if lst[i] == lst[j]:
                break
            j += 1
        if j == len(lst):
            return lst[i]
    return -1


def main():
    print(find_first_unique([9,2,3,3,9,6]))
    
    print(find_first_unique([9,2,3,2,6,6]))
    print(find_first_unique([4,5,1,5,4]))
    print(find_first_unique([0,0,1]))
    
    
    
    
if __name__ == "__main__":
    main()