from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # num of devices in last line
        lastNumOfDevices = 0
        ans = 0
        for row in bank:
            numOfDevices = row.count('1')
            if numOfDevices == 0:
                continue
            ans += lastNumOfDevices * numOfDevices
            lastNumOfDevices = numOfDevices
        return ans
    
s = Solution()
print(s.numberOfBeams(["011001","000000","010100","001000"]))