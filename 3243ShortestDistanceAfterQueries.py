from typing import List
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dpFrom, dpTo = list(range(n)), list(range(n-1,-1,-1))