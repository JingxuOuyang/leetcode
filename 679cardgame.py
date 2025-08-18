from typing import List

def check(a:int, b:int)->List[int]:
    return [a+b, a*b, a-b, b-a, a/b if b != 0 else None, b/a if a != 0 else None]

def exchangableResults(a,b):
    if isinstance(a, list) and isinstance(b, list):
        # 列表情况：返回两个列表的组合
        return [x + y for x, y in zip(a, b)] + [x * y for x, y in zip(a, b)]
    else:
        # 整数情况：返回包含两个结果的列表
        return [a + b, a * b]

def unexchangableResults(a,b):
    # 处理列表类型
    if isinstance(a, list) and isinstance(b, list):
        results = []
        # 遍历每个元素对
        for x, y in zip(a, b):
            results.append(x + y)    # a+b
            results.append(x * y)    # a*b
            results.append(x - y)    # a-b
            results.append(y - x)    # b-a
            if y != 0:
                results.append(x / y)  # a/b
            if x != 0:
                results.append(y / x)  # b/a
        return results
    # 处理整数类型
    else:
        results = [
            a + b,    # a+b
            a * b,    # a*b
            a - b,    # a-b
            b - a     # b-a
        ]
        if b != 0:
            results.append(a / b)  # a/b
        if a != 0:
            results.append(b / a)  # b/a
        return results

def unexchangableResults2(a,b,c):
    return unexchangableResults(unexchangableResults(a, b),c)

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        target = 24
        EPSILON = 1e-6
        def step(stk:List[int], nextCard:int, cardSeq:List[int]):
            if len(stk) >= 2:
                for i in range(4):
                    if i == 0:
                        val = stk[-1] + stk[-2]
                    elif i == 1:
                        val = stk[-2] - stk[-1]
                    elif i == 2:
                        val = stk[-1] * stk[-2]
                    else:
                        if stk[-1] == 0:
                            continue
                        val = stk[-2] / stk[-1]
                    if nextCard == 4 and len(stk) == 2:
                        if abs(val - target) < EPSILON:
                            return True
                    else:
                        t1, t2 = stk[-1], stk[-2]
                        stk.pop()
                        stk[-1] = val
                        if step(stk, nextCard, cardSeq):
                            return True
                        stk[-1] = t2
                        stk.append(t1)
            if nextCard < 4:
                stk.append(cards[cardSeq[nextCard]])
                if step(stk, nextCard + 1, cardSeq):
                    return True
                stk.pop()
            else:
                return False
        if step([], 0, [0, 1, 2, 3]):
            return True
        if step([], 0, [0, 1, 3, 2]):
            return True
        if step([], 0, [0, 2, 1, 3]):
            return True
        if step([], 0, [0, 2, 3, 1]):
            return True
        if step([], 0, [0, 3, 1, 2]):
            return True
        if step([], 0, [0, 3, 2, 1]):
            return True
        if step([], 0, [1, 0, 2, 3]):
            return True
        if step([], 0, [1, 0, 3, 2]):
            return True
        if step([], 0, [1, 2, 0, 3]):
            return True
        if step([], 0, [1, 2, 3, 0]):
            return True
        if step([], 0, [1, 3, 0, 2]):
            return True
        if step([], 0, [1, 3, 2, 0]):
            return True
        if step([], 0, [2, 0, 1, 3]):
            return True
        if step([], 0, [2, 0, 3, 1]):
            return True
        if step([], 0, [2, 1, 0, 3]):
            return True
        if step([], 0, [2, 1, 3, 0]):
            return True
        if step([], 0, [2, 3, 0, 1]):
            return True
        if step([], 0, [2, 3, 1, 0]):
            return True
        if step([], 0, [3, 0, 1, 2]):
            return True
        if step([], 0, [3, 0, 2, 1]):
            return True
        if step([], 0, [3, 1, 0, 2]):
            return True
        if step([], 0, [3, 1, 2, 0]):
            return True
        if step([], 0, [3, 2, 0, 1]):
            return True
        if step([], 0, [3, 2, 1, 0]):
            return True
        return False

s = Solution()
#print(s.judgePoint24([4, 1, 8, 7]))
#print(s.judgePoint24([1, 2, 1, 2]))
print(s.judgePoint24([1,9,2,1]))