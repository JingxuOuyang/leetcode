class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n2 = num2.bit_count()
        n1 = num1.bit_count()
        if n1 == n2:
            return num1
        if n1 > n2:
            # high 1 bit to 0 = 
            mask, c = 1, 0
            while c < n1 - n2:
                if mask & num1 > 0:
                    num1 ^= mask
                    c += 1
                mask <<= 1
            return num1
        mask, c = 1, 0
        while c < n2 - n1:
            if mask & num1 == 0:
                num1 |= mask
                c += 1
            mask <<= 1
        return num1
    
if __name__ == '__main__':
    s = Solution()
    print(s.minimizeXor(num1 = 3, num2 = 5))
    print(s.minimizeXor(num1 = 1, num2 = 12))
    print(s.minimizeXor(7, 16))
    print(s.minimizeXor(25, 72))