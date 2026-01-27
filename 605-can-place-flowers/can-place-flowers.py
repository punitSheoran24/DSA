class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n==0:
            return True
        if len(flowerbed)<2:
            if flowerbed[0]==0:
                flowerbed[0]=1
                n-=1

        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        length = len(flowerbed) - 1
        i = 1
        while n and i < length:
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            i += 1
        if n and flowerbed[len(flowerbed) - 1] == 0 and flowerbed[len(flowerbed) - 2] == 0:
            flowerbed[len(flowerbed) - 1] = 1
            n -= 1
        if not n:
            return True
        return False