class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1
    
if __name__ == "__main__":
    s = Solution()
    print(s.isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg"))