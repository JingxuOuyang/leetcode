class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + (k-1).bit_count())

s = Solution()
print(s.kthCharacter(5)) #b
print(s.kthCharacter(10)) #c