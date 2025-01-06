from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        a, na = 0, 0
        n = len(boxes)
        b, nb = 0, 0
        for i in range(n - 1, -1, -1):
            b += nb
            if boxes[i] == '1':
                nb += 1
        ans = [0] * n
        for i in range(n):
            if boxes[i] == '1':
                nb -= 1
            b -= nb
            ans[i] = a + b + na + nb
            a += na
            if boxes[i] == '1':
                na += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minOperations(boxes = "110"))
    print(s.minOperations("001011"))