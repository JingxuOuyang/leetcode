class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        maxIndex = 0
        cord = ord(word[0])
        n = len(word)
        i = 1
        while i < n:
            t = ord(word[i])
            if t > cord:
                maxIndex = i
                cord = t
            elif t == cord:
                for j in range(1, i - maxIndex):
                    if i + j >= n:
                        break
                    tj = ord(word[i + j])
                    if tj > cord:
                        maxIndex = i + j
                        cord = tj
                        i += j
                        break
                    tc = ord(word[maxIndex + j])
                    if tc > tj:
                        i += j
                        break
                    if tc < tj:
                        maxIndex = i
                        i += j
                        break
            i += 1

        if maxIndex >= numFriends - 1:
            return word[maxIndex:]
        return word[maxIndex:-(numFriends - maxIndex - 1)]

s = Solution()
#print(s.answerString('abcde', 2)) # Output: 'e'
#print(s.answerString('dbca', 2))
#print(s.answerString("nbjnc", 2))
print(s.answerString('djajdgc', 4))