from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = sorted(filter(lambda x: x <= n, banned))
        ans = 0
        a = 1
        i = 0
        while maxSum > 0 and i < len(banned):
            if a >= banned[i]:
                a = banned[i] + 1
                i += 1
                continue
            blockSum = (a + banned[i] - 1)*(banned[i] - a) // 2
            if blockSum <= maxSum:
                maxSum -= blockSum
                ans += banned[i] - a
                a = banned[i] + 1
                i += 1
            else:
                l, r = a, banned[i] - 1
                while l <= r:
                    mid = (l + r) // 2
                    testSum = (a + mid) * (mid - a + 1) // 2
                    if testSum == maxSum:
                        r = mid
                        break
                    elif testSum < maxSum:
                        l = mid + 1
                    else:
                        r = mid - 1
                ans += r - a + 1
                return ans
        if maxSum > 0:
            if len(banned) > 0:
                l, r = banned[-1] + 1, n
            else:
                l, r = 1, n
            a = l
            while l <= r:
                mid = (l + r) // 2
                testSum = (a + mid) * (mid - a + 1) // 2
                if testSum == maxSum:
                    r = mid
                    break
                elif testSum < maxSum:
                    l = mid + 1
                else:
                    r = mid - 1
            ans += r - a + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    # 3953
    print(s.maxCount([179,266,77,196,59,313,286,41,21,201,57,237,74,333,101,281,227,25,138,10,304,55,50,72,244,113,159,330,154,156,311,170,283,9,224,46,197,2,325,237,54,168,275,166,236,30,250,48,274,331,240,153,312,63,303,342,79,37,165,20,79,293,103,152,215,44,56,196,29,251,264,210,212,135,296,123,289,257,208,309,67,114,170,119,337,163,242,162,109,318,51,105,272,240,107,226,224,188,224,317,27,102,63,128,3,133,27,134,186,220,198,24,274,287,267,8,13,322,278,166,304,165,342,89,184,300,312,339,163,307,123,137,293,227,229,57,66,13,71,233,260,79,228,301,4,4,89,196,193,337,205,51,144,99,104,73,10,311,240,168,77,244,114,217,186,134,229,241,46,89,54,127], 4085, 109718563))
    # 9
    #print(s.maxCount([87,193,85,55,14,69,26,133,171,180,4,8,29,121,182,78,157,53,26,7,117,138,57,167,8,103,32,110,15,190,139,16,49,138,68,69,92,89,140,149,107,104,2,135,193,87,21,194,192,9,161,188,73,84,83,31,86,33,138,63,127,73,114,32,66,64,19,175,108,80,176,52,124,94,33,55,130,147,39,76,22,112,113,136,100,134,155,40,170,144,37,43,151,137,82,127,73], 1079, 87))
    # print(s.maxCount(banned = [1,6,5], n = 5, maxSum = 6))
    # print(s.maxCount(banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1))
    # print(s.maxCount(banned = [11], n = 7, maxSum = 50))
    # 17
    #print(s.maxCount([176,36,104,125,188,152,101,47,51,65,39,174,29,55,13,138,79,81,175,178,42,108,24,80,183,190,123,20,139,22,140,62,58,137,68,148,172,76,173,189,151,186,153,57,142,105,133,114,165,118,56,59,124,82,49,94,8,146,109,14,85,44,60,181,95,23,150,97,28,182,157,46,160,155,12,67,135,117,2,25,74,91,71,98,127,120,130,107,168,18,69,110,61,147,145,38], 3016, 240))