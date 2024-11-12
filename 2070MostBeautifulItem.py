from typing import List
import bisect

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        n = len(items)
        sortedIndexArr = list(range(n))
        sortedIndexArr.sort(key=lambda idx: items[idx][0])
        sortedPrices, sortedBeauties = [0] * n, [0] * n
        lastMaxBeauty = 0
        for i, idx in enumerate(sortedIndexArr):
            sortedPrices[i] = items[idx][0]
            sortedBeauties[i] = max(lastMaxBeauty, items[idx][1])
            lastMaxBeauty = sortedBeauties[i]
        ans = []
        for query in queries:
            queryIdx = bisect.bisect_right(sortedPrices, query)
            if queryIdx == 0:
                ans.append(0)
                continue
            ans.append(sortedBeauties[queryIdx - 1])
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))
    print(s.maximumBeauty(items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]))