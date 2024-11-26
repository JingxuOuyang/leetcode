from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        possibleChampions = [True] * n
        for edge in edges:
            possibleChampions[edge[1]] = False
        if possibleChampions.count(True) == 1:
            return possibleChampions.index(True)
        return -1
    
if __name__ == "__main__":
    s = Solution()
    print(s.findChampion(n = 3, edges = [[0,1],[1,2]]))
    print(s.findChampion(n = 4, edges = [[0,2],[1,3],[1,2]]))