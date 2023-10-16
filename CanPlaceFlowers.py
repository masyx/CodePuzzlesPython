class Solution:
    # O(n) time | O(1) space
    def can_place_flowers(self, flowerbed, n):
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) \
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0
    

def main():
    sol = Solution()
    print(sol.can_place_flowers([0, 0, 0], 2))
    
if __name__ == "__main__":
    main()