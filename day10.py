def solution1(inp: str) -> int:
    open_ = '([{<'
    close = ')]}>'
    d_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    res = 0
    for row in inp.strip().split('\n'):
        stack = []
        for char in row:
            if char in open_:
                stack.append(char)
            elif char in close:
                if stack:
                    last = stack.pop()
                else:
                    res += d_points[char]
                    break
                if open_.find(last) != close.find(char):
                    res += d_points[char]
                    break
    return res


def solution2(inp: str) -> int:
    open_ = '([{<'
    close = ')]}>'
    vals = []
    for row in inp.strip().split('\n'):
        stack = []
        for char in row:
            if char in open_:
                stack.append(char)
            elif char in close:
                if stack:
                    last = stack.pop()
                else:
                    break
                if open_.find(last) != close.find(char):
                    break
        else:
            val = 0
            d_points = {')': 1, ']': 2, '}': 3, '>': 4}
            for char in stack[::-1]:
                val *= 5
                val += d_points[close[open_.find(char)]]
            vals.append(val)
    vals.sort()
    return vals[len(vals) // 2]


with open('input/input10.txt') as f:
    inp = f.read()

print(solution1(inp))
print(solution2(inp))
