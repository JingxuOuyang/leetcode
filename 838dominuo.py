class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = list()
        n = len(dominoes)
        i = 0
        while i < n:
            j = i
            while i < n and dominoes[i] == '.':
                i += 1
            if n == i:
                for k in range(i - j):
                    ans.append('.')
                break
            if dominoes[i] == 'L':
                for k in range(i - j):
                    ans.append('L')
                ans.append('L')
            else:
                for k in range(i - j):
                    ans.append('.')
                j = i
                i += 1                
                while i < n:
                    if dominoes[i] == 'R':
                        for k in range(i - j):
                            ans.append('R')
                        j = i
                        i += 1
                    elif dominoes[i] == 'L':
                        merge_len = i - j + 1
                        for k in range(merge_len//2):
                            ans.append('R')
                        if merge_len % 2 == 1:
                            ans.append('.')
                        for k in range(merge_len//2):
                            ans.append('L')
                        break
                    else:
                        i += 1
                if i == n:
                    for k in range(n - j):
                        ans.append('R')
            i += 1
        return ''.join(ans)

s = Solution()
print(s.pushDominoes('..L'))