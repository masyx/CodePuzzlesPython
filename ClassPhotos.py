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
    


def main():
    blueShirts = [5,8,1,3,4]
    redShirts = [6,9,2,4,5]
    print(classPhotos(redShirts, blueShirts))
    
    
if __name__ == "__main__":
    main()