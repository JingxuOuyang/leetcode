from typing import List
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        #n = len(rectangles)
        rectangles.sort(key=lambda x: x[1])
        bline = -1
        lastLine = 0
        #for i in range(n):
        #    rect = rectangles[i]
        for rect in rectangles:
            if rect[1] >= lastLine:
                bline += 1
                if bline == 2:
                    return True 
            if rect[3] > lastLine:
                lastLine = rect[3]

        rectangles.sort(key=lambda x: x[0])
        bline = -1
        lastLine = 0
        for rect in rectangles:
            if rect[0] >= lastLine:
                bline += 1
                if bline == 2:
                    return True 
            if rect[2] > lastLine:
                lastLine = rect[2]
        return False

s = Solution()
print(s.checkValidCuts(n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(s.checkValidCuts(n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]))