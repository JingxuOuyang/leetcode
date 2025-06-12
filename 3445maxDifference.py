class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        chr_set = [chr(i) for i in range(ord('0'), ord('5'))]
        def get_state(a, b):
            return ((a & 1) << 1) + (b & 1)
        ans = -10 ** 5
        for a in chr_set:
            for b in chr_set:
                if a == b:
                    continue
                left = -1
                prev_a, prev_b = 0, 0
                count_a, count_b = 0, 0
                bests = [float('inf')] * 4
                for right in range(n):
                    count_a += (s[right] == a)
                    count_b += (s[right] == b)
                    while right - left >= k and count_b - prev_b >= 2:
                        t = prev_a - prev_b
                        prev_state = get_state(prev_a, prev_b)
                        if t < bests[prev_state]:
                            bests[prev_state] = t
                        left += 1
                        prev_b += (s[left] == b)
                        prev_a += (s[left] == a)
                    right_state = get_state(count_a, count_b)
                    if bests[(right_state ^ 2)] != float('inf'):
                        val = count_a - count_b - bests[(right_state ^ 2)]
                        if val > ans:
                            ans = val
        return ans

s = Solution()
print(s.maxDifference(s = "12233", k = 4))
print(s.maxDifference(s = "1122211", k = 3))