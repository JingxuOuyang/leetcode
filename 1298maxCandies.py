from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        owned = [False] * n
        q = deque()
        ans = 0
        def draw(box : int):
            if not owned[box]:
                return 0
            if status[box] == 0:
                return 0
            if candies[box] == 0:
                return 0
            candy = candies[box]
            candies[box] = 0
            for key in keys[box]:
                status[key] = 1
                candy += draw(key)
            for box2 in containedBoxes[box]:
                owned[box2] = True
                candy += draw(box2)
            return candy
        
        for box in initialBoxes:
            owned[box] = True
            ans += draw(box)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0])) #16
    print(s.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))
