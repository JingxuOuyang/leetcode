from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        a = ord('a')
        counts = [0] * 26
        for word in words2:
            wordCounts = [0] * 26
            for c in word:
                wordCounts[ord(c) - a] += 1
            for i in range(26):
                if wordCounts[i] > counts[i]:
                    counts[i] = wordCounts[i]
        ans = []
        for word in words1:
            wordCounts = [0] * 26
            for c in word:
                wordCounts[ord(c) - a] += 1
            bUniversal = True
            for i in range(26):
                if wordCounts[i] < counts[i]:
                    bUniversal = False
                    break
            if bUniversal:
                ans.append(word)
        return ans
    
if __name__ == '__main__':
    s = Solution()
    print(s.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]))
    print(s.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]))