from typing import List
import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        negGifts = [-x for x in gifts]
        heapq.heapify(negGifts)
        for i in range(k):
            t = math.isqrt(-negGifts[0])
            heapq.heappushpop(negGifts, -t)
        return -sum(negGifts)
            
if __name__ == '__main__':
    s = Solution()
    print(s.pickGifts(gifts = [25,64,9,4,100], k = 4))
    print(s.pickGifts(gifts = [1,1,1,1], k = 4))