from typing import List
from collections import deque 
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Create a copy of prices array to store discounted prices
        result = prices.copy()

        stack = deque()

        for i in range(len(prices)):
            # Process items that can be discounted by current price
            while stack and prices[stack[-1]] >= prices[i]:
                # Apply discount to previous item using current price
                result[stack.pop()] -= prices[i]
            # Add current index to stack
            stack.append(i)

        return result

if __name__ == '__main__':
    s = Solution()
    print(s.finalPrices(prices = [8,4,6,2,3]))