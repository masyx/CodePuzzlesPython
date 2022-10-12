def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    red_shirts_in_front = redShirtHeights[0] > blueShirtHeights[0]
    for i in range(len(redShirtHeights)):
        if red_shirts_in_front:
            if redShirtHeights[i] <= blueShirtHeights[i]:
                return False
        else:
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
    return True


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[0] > blueShirtHeights[0]:
        return arrange_photo(redShirtHeights, blueShirtHeights)
    else:
        return arrange_photo(blueShirtHeights, redShirtHeights)
    
def arrange_photo(tallerGroup, smallerGroup):
    for i in range(len(tallerGroup)):
        if tallerGroup[i] <= smallerGroup[i]:
            return False
    return True

def main():
    redShirts = [5, 8, 1, 3, 4]
    blueShirts = [6, 9, 2, 4, 5]
    print(classPhotos(redShirts, blueShirts))

if __name__ == '__main__':
    main()