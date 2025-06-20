from collections import namedtuple
class State:
    def __init__(self, k):
        self.x, self.y = 0, 0
        self.k = k
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        states = [State(k), State(k), State(k), State(k)] 
        for c in s:
            if c == 'N':
                states[0].y += 1
                states[1].y += 1
                if states[2].k > 0:
                    states[2].y -= 1
                    states[2].k -= 1
                else:
                    states[2].y += 1
                if states[3].k > 0:
                    states[3].y -= 1
                    states[3].k -= 1
                else:
                    states[3].y += 1
            elif c == 'S':
                states[2].y -= 1
                states[3].y -= 1
                if states[0].k > 0:
                    states[0].y += 1
                    states[0].k -= 1
                else:
                    states[0].y -= 1
                if states[1].k > 0:
                    states[1].y += 1
                    states[1].k -= 1
                else:
                    states[1].y -= 1
            elif c == 'E':
                states[0].x += 1
                states[3].x += 1
                if states[1].k > 0:
                    states[1].x -= 1
                    states[1].k -= 1
                else:
                    states[1].x += 1
                if states[2].k > 0:
                    states[2].x -= 1
                    states[2].k -= 1
                else:
                    states[2].x += 1
            else: # W
                states[1].x -= 1
                states[2].x -= 1
                if states[0].k > 0:
                    states[0].x += 1
                    states[0].k -= 1
                else:
                    states[0].x -= 1
                if states[3].k > 0:
                    states[3].x += 1
                    states[3].k -= 1
                else:
                    states[3].x -= 1
            print(f'{states[0].x},{states[0].y} {states[1].x},{states[1].y} {states[2].x},{states[2].y} {states[3].x},{states[3].y}')

            ans = max(ans, max([abs(state.x) + abs(state.y) for state in states]))
        return ans

s = Solution()
print(s.maxDistance("NSES", 1))