class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        hasYuanyin, hasFuyin = False, False
        for c in word:
            if not c.isalpha():
                continue
            if hasYuanyin and hasFuyin:
                break
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                hasYuanyin = True
            else:
                hasFuyin = True
        return hasFuyin and hasYuanyin