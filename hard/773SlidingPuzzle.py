from typing import List

def boardState(board: List[List[int]]):
    return tuple([tuple(board[0]), tuple(board[1])])

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        finalState = ((1,2,3),(4,5,0))
        if boardState(board) == finalState:
            return 0
        seen = set()
        seen.add(boardState(board))
        curBoards = [board]
        
        ans = 1
        while len(curBoards) > 0:
            nextBoards = []
            for curboardState in curBoards:
                zerox, zeroy = -1, -1
                for y in range(2):
                    if zerox != -1:
                        break
                    for x in range(3):
                        if curboardState[y][x] == 0:
                            zeroy = y
                            zerox = x
                            break
                if zerox > 0:
                    newState = [[0]*3, [0]*3]
                    for y in range(2):
                        for x in range(3):
                            newState[y][x] = curboardState[y][x]
                    newState[zeroy][zerox] = newState[zeroy][zerox - 1]
                    newState[zeroy][zerox - 1] = 0
                    newTurpleState = boardState(newState)
                    if newTurpleState == finalState:
                        return ans
                    if newTurpleState not in seen:
                        nextBoards.append(newState)
                        seen.add(newTurpleState)
                if zerox < 2:
                    newState = [[0]*3, [0]*3]
                    for y in range(2):
                        for x in range(3):
                            newState[y][x] = curboardState[y][x]
                    newState[zeroy][zerox] = newState[zeroy][zerox + 1]
                    newState[zeroy][zerox + 1] = 0
                    newTurpleState = boardState(newState)
                    if newTurpleState == finalState:
                        return ans
                    if newTurpleState not in seen:
                        nextBoards.append(newState)
                        seen.add(newTurpleState)
                if zeroy == 1:
                    newState = [[0]*3, [0]*3]
                    for y in range(2):
                        for x in range(3):
                            newState[y][x] = curboardState[y][x]
                    newState[zeroy][zerox] = newState[zeroy - 1][zerox]
                    newState[zeroy - 1][zerox] = 0
                    newTurpleState = boardState(newState)
                    if newTurpleState == finalState:
                        return ans
                    if newTurpleState not in seen:
                        nextBoards.append(newState)
                        seen.add(newTurpleState)
                else:
                    newState = [[0]*3, [0]*3]
                    for y in range(2):
                        for x in range(3):
                            newState[y][x] = curboardState[y][x]
                    newState[zeroy][zerox] = newState[zeroy + 1][zerox]
                    newState[zeroy + 1][zerox] = 0
                    newTurpleState = boardState(newState)
                    if newTurpleState == finalState:
                        return ans
                    if newTurpleState not in seen:
                        nextBoards.append(newState)
                        seen.add(newTurpleState)
            curBoards = nextBoards
            ans += 1
        return -1
    
if __name__ == "__main__":
    s = Solution()
    #print(s.slidingPuzzle(board = [[1,2,3],[4,0,5]]))
    #print(s.slidingPuzzle(board = [[1,2,3],[5,4,0]]))
    print(s.slidingPuzzle(board = [[4,1,2],[5,0,3]]))