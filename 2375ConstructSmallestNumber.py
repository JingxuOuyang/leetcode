
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        sortArr = [0]
        lastIndex = 0
        for i, c in enumerate(pattern):
            if c == 'I':
                sortArr.append(i + 1)
                lastIndex = len(sortArr) - 1
            else:
                sortArr.insert(lastIndex, i + 1)
        n = len(sortArr)
        ans = []
        for i in range(n):
            ans.append('')
        base = ord('1')
        for sortIdx, idx in enumerate(sortArr):
            ans[idx] = chr(base + sortIdx)
        return ''.join(ans)
    
s = Solution()
print(s.smallestNumber(pattern = "IIIDIDDD"))