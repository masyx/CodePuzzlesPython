# O(n log(n)) time | O(1) space
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    fastestTotalSpeed = 0
    if fastest:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse = True)
        for i in range(len(redShirtSpeeds)):
            fastestTotalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
        return fastestTotalSpeed
            
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    for i in range(len(redShirtSpeeds)):
        fastestTotalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return fastestTotalSpeed


def tandemBicycle2(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    
    if fastest:
        reverseArray(blueShirtSpeeds)
    
    totalSpeed = 0    
    for i in range(len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return totalSpeed    
    
def reverseArray(array):
    left = 0
    right = len(array) - 1
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    
def main():
    redShirtSpeeds = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    print(tandemBicycle2(redShirtSpeeds, blueShirtSpeeds, True))
    
if __name__ == "__main__":
    main()