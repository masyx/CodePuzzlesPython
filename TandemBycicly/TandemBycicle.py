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

def main():
    redShirtSpeeds = [5, 5, 3, 9, 2]
    blueShirtSpeeds = [3, 6, 7, 2, 1]
    print(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, False))
    
if __name__ == "__main__":
    main()