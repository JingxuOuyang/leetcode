class Solution:
    def maxDifference(self, s: str) -> int:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        maxOdd, minEven = 0, len(s)
        for count in counts:
            if count == 0:
                continue
            if (count & 1) == 0:
                if count < minEven:
                    minEven = count
            else:
                if count > maxOdd:
                    maxOdd = count
        return maxOdd - minEven


s = Solution()
print(s.maxDifference("aaaaabbc"))
