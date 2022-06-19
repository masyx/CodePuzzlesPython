

def main():
    print("hi")
    
def sortedSquaredArray(array):
    squaredArray = []
    for i in range(len(array)):
        squaredArray.append(array[i]**2)
    
    squaredArray.sort()    
    return squaredArray





if __name__ == "__main__":
    main()