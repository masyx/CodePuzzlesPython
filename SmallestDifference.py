# medium

# O(n*log(n) + m*log(m)) time | O(1) space
def smallestDifference(array_one, array_two):
    array_one.sort()
    array_two.sort()
    i = 0
    j = 0
    result = []
    smallest_dif = float('inf')
    while i < len(array_one) and  j < len(array_two):
        first_num = array_one[i]
        second_num = array_two[j]
        current_dif = abs(first_num - second_num)
        if current_dif == 0:
            return [first_num, second_num]
        elif first_num < second_num:
            i += 1
        else:
            j += 1
        if smallest_dif > current_dif:
            smallest_dif = current_dif
            result = [first_num, second_num]
    return result
    

def main():
    # [-1, 3, 5, 10, 20, 28]
    # [15, 17, 26, 134, 134]
    array_one = [-1, 5, 10, 20, 3]
    array_two = [26, 134, 135, 15, 17]
    print(smallestDifference(array_one, array_two))
    
    
if __name__ == "__main__":
    main()