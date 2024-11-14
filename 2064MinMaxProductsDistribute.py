from typing import List
class Solution:
    # it's ok, the alternative solution is maxheap
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # binary search?
        sum, r = 0, 0
        for quantity in quantities:
            sum += quantity
            if quantity > r:
                r = quantity
        l = (sum - 1) // n + 1
        while l <= r:
            mid = (l + r) // 2
            stores = 0
            for quantity in quantities:
                stores += (quantity - 1) // mid + 1
                if  stores > n:
                    break
            if stores <= n:
                r = mid - 1
            else: 
                l = mid + 1
        return l

if __name__ == "__main__":
    s = Solution()
    print(s.minimizedMaximum(n = 6, quantities = [11,6]))
    print(s.minimizedMaximum(n = 7, quantities = [15,10,10]))
    print(s.minimizedMaximum(n = 1, quantities = [100000]))