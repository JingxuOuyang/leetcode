from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        freeTimes = [0] * (n + 1)
        meetTimes = [0] * n
        maxLeftFreeTimes = [0] * (n + 1)
        maxRightFreeTimes = [0] * (n + 1)
        lastMeetingEndTime = 0
        for i in range(n):
            freeTimes[i] = startTime[i] - lastMeetingEndTime
            meetTimes[i] = endTime[i] - startTime[i]
            lastMeetingEndTime = endTime[i]
        freeTimes[-1] = eventTime - lastMeetingEndTime
        maxLeftFreeTimes[0] = freeTimes[0]
        maxRightFreeTimes[-1] = freeTimes[-1]
        for i in range(1, n + 1):
            maxLeftFreeTimes[i] = max(freeTimes[i], maxLeftFreeTimes[i - 1])
        for i in range(n - 1, -1, -1):
            maxRightFreeTimes[i] = max(freeTimes[i], maxRightFreeTimes[i + 1])
        ans = 0
        for i in range(n):
            maxLeft, maxRight = 0 if i == 0 else maxLeftFreeTimes[i - 1], 0 if i == n - 1 else maxRightFreeTimes[i + 2]
            if maxLeft >= meetTimes[i] or maxRight >= meetTimes[i]:
                maxFreeTimeI = freeTimes[i] + freeTimes[i + 1] + meetTimes[i]
            else:
                maxFreeTimeI = freeTimes[i] + freeTimes[i + 1]
            if maxFreeTimeI > ans:
                ans = maxFreeTimeI
        return ans
