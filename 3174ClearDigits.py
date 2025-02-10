class Solution:
    def clearDigits(self, s: str) -> str:
        count = []
        for c in s:
            if c.isdigit():
                count.pop()
            else:
                count.append(c)
        return "".join(count)

if __name__ == '__main__':
    s = Solution()
    print(s.clearDigits('abc'))
    print(s.clearDigits('cb34'))