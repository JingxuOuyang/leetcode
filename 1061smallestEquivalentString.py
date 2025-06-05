class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        equivalences = [i for i in range(26)]
        def findRoot(i:int)->int:
            while i != equivalences[i]:
                i = equivalences[i]
            return i
        n = len(s1)
        for i in range(n):
            a, b = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            if a == b:
                continue
            a, b = findRoot(a), findRoot(b)
            if b < a:
                equivalences[a] = b
            else:
                equivalences[b] = a
        ans = []
        for c in baseStr:
            a = ord(c) - ord('a')
            ans.append(chr(findRoot(a) + ord('a')))
        return ''.join(ans)

s = Solution()
print(s.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser")) #"makkek"
print(s.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold")) #"hdld"
print(s.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode")) #"aauaaaaada"