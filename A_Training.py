class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    total_speed = 0
    if fastest:
        reverse_array(redShirtSpeeds)
    for i in range(len(redShirtSpeeds)):
        total_speed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return total_speed

def reverse_array(list):
    l, r = 0, len(list) - 1
    while l < r:
        list[l], list[r] = list[r], list[l]
        l += 1
        r -= 1

def main():
    red = [5, 5, 3, 9, 2]
    blue = [3, 6, 7, 2, 1]
    print(tandemBicycle(red, blue, True))


main()