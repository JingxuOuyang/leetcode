from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        j = 0
        ans = []
        for i in range(n):
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(s[i])
        return ''.join(ans)
    
if __name__ == '__main__':
    s = Solution()
    print(s.addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
    print(s.addSpaces(s = "icodeinpython", spaces = [1,5,7,9]))
    print(s.addSpaces(s = "spacing", spaces = [0,1,2,3,4,5,6]))