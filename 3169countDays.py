from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = [meeting for meeting in meetings if meeting[0] <= days]
        meetings.sort(key=lambda x:x[0])
        lastMeetDay = 0
        ans = 0
        for meet in meetings:
            if meet[0] > lastMeetDay:
                ans += meet[0] - lastMeetDay - 1
            lastMeetDay = max(lastMeetDay, meet[1])
            if lastMeetDay > days:
                break
        if lastMeetDay < days:
            ans += days - lastMeetDay
        return ans

s = Solution()
print(s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]])) #2