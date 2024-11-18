from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        if k > 0:
            klist = code[0:k]
            ksum = sum(klist)
            for i in range(n - k):
                ksum += code[i + k] - code[i]
                code[i] = ksum
            for i in range(n - k, n):
                ksum += klist[i - n + k] - code[i]
                code[i] = ksum
            return code
        else:
            klist = code[k:]
            ksum = sum(klist)
            for i in range(-1, -(n + k + 1), -1):
                ksum += code[i + k] - code[i]
                code[i] = ksum
            for i in range(-(n + k + 1), -n-1, -1):
                ksum += klist[i + n + k] - code[i]
                code[i] = ksum
            return code

if __name__ == "__main__":
    s = Solution()
#     Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
# Example 2:

# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0. 
# Example 3:

# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
    print(s.decrypt(code = [5,7,1,4], k = 3))
    print(s.decrypt(code = [1,2,3,4], k = 0))
    print(s.decrypt(code = [2,4,9,3], k = -2))         