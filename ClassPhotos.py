# O(n log(n)) time | O(1) space
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[-1] > blueShirtHeights[-1]:
        return arrangePhoto(redShirtHeights, blueShirtHeights)
    else:
        return arrangePhoto(blueShirtHeights, redShirtHeights)
        
def arrangePhoto(tallerGroup, smallerGroup):
    for i in range(len(tallerGroup)):
        if tallerGroup[i] <= smallerGroup[i]:
            return False
    return True
    
    
def classPhotosAlgo(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    
    groupInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
    
    for idx in range(len(redShirtHeights)):
        if groupInFirstRow == 'RED':
            if redShirtHeights[idx] >= blueShirtHeights[idx]:
                return False
        else:
            if blueShirtHeights[idx] >= redShirtHeights[idx]:
                return False
    return True


def main():
    blueShirts = [5,8,1,3,4]
    redShirts = [6,9,2,4,5]
    print(classPhotoAlgo(redShirts, blueShirts))
    
    
if __name__ == "__main__":
    main()