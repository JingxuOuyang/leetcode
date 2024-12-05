from typing import List

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i, j = 0, 0
        while i < n:
            while i < n and start[i] == '_':
                i += 1
            if i == n:
                break
            while j < n and target[j] == '_':
                j += 1
            if j == n:
                return False
            if start[i] != target[j]:
                return False
            if start[i] == 'L':
                if i < j:
                    return False
            else:
                if i > j:
                    return False
            i += 1
            j += 1
        while j < n:
            if target[j] != '_':
                return False
            j += 1
        return True

if __name__ == '__main__':
    s = Solution()
    #print(s.canChange(start = "_L__R__R_", target = "L______RR"))
    #print(s.canChange(start = "R_L_", target = "__LR"))
    #print(s.canChange(start = "_R", target = "R_"))
    print(s.canChange("___LL", "LL___"))