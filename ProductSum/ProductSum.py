# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, depth = 1):
    currentSum = 0
    for i in range(len(array)):
        if type(array[i]) is int:
            currentSum += array[i]
        else:
            sum = productSum(array[i], depth + 1)
            currentSum += sum 
    currentSum *= depth
    return currentSum



def main():
    array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    #array = [1,3,[4,-1],1] # 11
    print(productSum(array))
    

if __name__ == "__main__":
    main() 