# 0  1  2 3 4 5
# -------------
# 1 -2 -1 0 4 2  target 0


# result = [[1, 3, 0], [-2, 4, 2]]
  
def two_sum(numbers, target):
    if not numbers:
        return []
    result = []
    seen = {}
    for number in numbers:
        possible_match = target - number
        if possible_match in seen:
            result.append([number, possible_match])
        seen[number] = True
    return result

def three_sum(numbers):
    if not numbers:
        return []
    result = {}
    for i in range(len(numbers)):
        seen = {}
        for j in range(i + 1, len(numbers)):
            possible_match = 0 - numbers[i] - numbers[j]
            if possible_match in seen:
                curr_result = sorted([numbers[i], numbers[j], possible_match])
                curr_result_tuple = tuple(curr_result)
                if curr_result_tuple not in result:
                    result[curr_result_tuple] = curr_result
            seen[numbers[j]] = True
    return list(result.values())
            
if __name__ == "__main__":
    numbers = [-1,0,1,2,-1,-4]
    print(three_sum(numbers))