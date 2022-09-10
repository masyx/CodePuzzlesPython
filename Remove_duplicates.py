#O(n) time | O(1) space
def remove_duplicates(arr):
    none_duplicate_pointer = 0
    for i in range(1, len(arr)):
        if arr[none_duplicate_pointer] != arr[i]:
            arr[none_duplicate_pointer + 1] = arr[i]
            none_duplicate_pointer += 1
    return none_duplicate_pointer + 1

#O(n) time | O(1) space
def remove_duplicates_2(arr):
  next_non_duplicate = 1
  i = 0
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1
  return next_non_duplicate


def main():
    arr = [2, 3, 3, 3, 6, 9, 9]
    print(remove_duplicates(arr))
    
    
if __name__ == "__main__":
    main()