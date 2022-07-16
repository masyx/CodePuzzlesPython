# O(n) time, O(d) space, where d is max depth of sub-arrays
def productSum(array, depth = 1):
    sum = 0
    for element in array:
        if type(element) is int:
            sum += element
        else:
            returnedSum = productSum(element, depth + 1)
            sum += returnedSum 
    sum *= depth
    return sum



def main():
    #array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
    #array = [1,3,[4,-1],1] # 11
    array = [1,3,[4,[2,6],-1],1] # 1+3+2*(4+3*(2+6)-1)+1 = 59
    print(productSum(array))
    

if __name__ == "__main__":
    main() 