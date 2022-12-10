def twoNumberSum(array, targetSum):
    seen_numbers = {}
    for idx, number in enumerate(array):
        possible_number = targetSum - number
        if possible_number in seen_numbers:
            return [number, possible_number]
        seen_numbers[number] = idx
    return []


def main():
    nums = [2, 3, 5, 11, 32]
    print(twoNumberSum(nums, 37))
    
    
if __name__ == "__main__":
    main()