class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    if fastest:
        total_speed = calculate_speed(sorted(redShirtSpeeds), \
            sorted(blueShirtSpeeds, reverse = True))
    else:
        total_speed = calculate_speed(sorted(redShirtSpeeds), \
            sorted(blueShirtSpeeds))
    return total_speed

def calculate_speed(first_team, second_team):
    total_speed = 0
    for i in range(len(first_team)):
            if first_team[i] > second_team[i]:
                total_speed += first_team[i]
            else:
                total_speed += second_team[i]
    return total_speed

def main():
    red = [5, 5, 3, 9, 2]
    blue = [3, 6, 7, 2, 1]
    print(tandemBicycle(red, blue, False))


main()