from typing import List
def head(x:int, y:int, dir:int):
    if dir == 0:
        return x + 1, y
    elif dir == 1:
        return x, y - 1
    elif dir == 2:
        return x - 1, y
    else:
        return x, y + 1

def turnLeft(dir:int):
    return (dir + 1) % 4

def turnRight(dir:int):
    return (dir - 1) % 4

def leftHand(x:int, y:int, dir:int):
    return head(x, y, turnLeft(dir))

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def oneMove(coordAndDir:List[int], walls:set)->bool:
            headx, heady = head(coordAndDir[0], coordAndDir[1], coordAndDir[2])
            if headx < 0 or headx >= n or heady < 0 or heady >= m or grid[heady][headx] == 1:
                if headx >= 0 and headx < n and heady >= 0 and heady < m:
                    walls.add((headx, heady))
                coordAndDir[2] = turnRight(coordAndDir[2])
                return False, headx, heady 
            else:
                headleftx, headlefty = leftHand(headx, heady, coordAndDir[2])
                if headleftx < 0 or headleftx >= n or headlefty < 0 or headlefty >= m or grid[headlefty][headleftx] == 1:
                    if headleftx >= 0 and headleftx < n and headlefty >= 0 and headlefty < m:
                        walls.add((headleftx, headlefty))
                    coordAndDir[0] = headx
                    coordAndDir[1] = heady
                    grid[heady][headx] = -1
                    return headx == n - 1 and heady == m - 1, headleftx, headlefty
                else:
                    coordAndDir[0] = headleftx
                    coordAndDir[1] = headlefty
                    coordAndDir[2] = turnLeft(coordAndDir[2])
                    grid[headlefty][headleftx] = -1
                    return headleftx == n - 1 and headlefty == m - 1, -1, -1

        def walkAlongObstacle(originalx:int, originaly:int, originaldir:int, walls:set)->bool:
            if originalx == n - 1 and originaly == m - 1:
                return True
            endWall = leftHand(originalx, originaly, originaldir)
            cur = [originalx, originaly, originaldir]
            while True:
                bReach, newWallX, newWallY = oneMove(cur, walls)
                if bReach:
                    return True
                if newWallX != -1 and newWallX == endWall[0] and newWallY == endWall[1]:
                    break
            return False    

        walls = set()
        grid[0][0] = -1
        if walkAlongObstacle(0, 0, 0, walls):
            return 0
        seenWalls = set()
        for wall in walls:
            seenWalls.add((wall[0], wall[1]))
        def checkWall(x:int, y:int, dir:int, walls:set)->bool:
            if grid[y][x] == -1:
                return False
            elif grid[y][x] == 1:
                if (x, y) not in seenWalls:
                    nextWalls.add((x, y))
                    seenWalls.add((x, y))
            else:
                if walkAlongObstacle(x, y, dir, walls):
                    return True
            return False
        
        ans = 1
        while len(walls) > 0:
            nextWalls = set()
            for wall in walls:
                wallx, wally = wall[0], wall[1]
                if wally > 0:
                    if checkWall(wallx, wally - 1, 2, nextWalls):
                        return ans
                if wally < m - 1:
                    if checkWall(wallx, wally + 1, 0, nextWalls):
                        return ans
                if wallx > 0:
                    if checkWall(wallx - 1, wally, 3, nextWalls):
                        return ans
                if wallx < n - 1:
                    if checkWall(wallx + 1, wally, 1, nextWalls):
                        return ans
            walls = nextWalls
            ans += 1
        return ans
    
if __name__ == "__main__":
    s = Solution()
    #print(s.minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]]))
    #print(s.minimumObstacles(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))
    print(s.minimumObstacles([[0,1,1,1,0]]))