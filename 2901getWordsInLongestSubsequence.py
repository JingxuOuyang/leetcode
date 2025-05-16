from typing import List
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        #n = len(words)
        dp = list()
        for i, word in enumerate(words):
            group = groups[i]
            maxLen, maxJ = 1, -1
            for j in range(i):
                if groups[j] == group:
                    continue
                wordj = words[j]
                if len(wordj) != len(word):
                    continue
                dis = 0
                for k in range(len(word)):
                    if word[k] != wordj[k]:
                        dis += 1
                        if dis > 1:
                            break
                if dis == 1:
                    l = dp[j][0] + 1
                    if l > maxLen:
                        maxLen = l
                        maxJ = j
            dp.append((maxLen, maxJ))
        index = max(range(len(dp)), key=lambda i: dp[i][0])
        ans = []
        while index >= 0:
            ans.append(words[index])
            index = dp[index][1]
        ans.reverse()
        return ans

s = Solution()
print(s.getWordsInLongestSubsequence(words = ["bab","dab","cab"], groups = [1,2,2]))
print(s.getWordsInLongestSubsequence(words = ["a","b","c","d"], groups = [1,2,3,4]))
print(s.getWordsInLongestSubsequence(["cb","dc","ab","aa","ac","bb","ca","bcc","cdd","aad","bba","bc","ddb"], [12,6,10,11,4,8,9,11,2,11,3,2,5]))