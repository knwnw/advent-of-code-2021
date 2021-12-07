def solution(inp: str) -> int:
    data = []
    for item in inp.split('\n'):
        for e in item.split(' -> '):
            data.extend(map(int, e.split(',')))

    n = len(data)
    field = [[0] * n for _ in range(n)]

    for k in range(0, n, 4):
        x1, y1, x2, y2 = data[k: k + 4]
        if x1 == x2:
            x, y = x1, min(y1, y2)
            for i in range(abs(y1 - y2) + 1):
                field[x][y + i] += 1
        elif y1 == y2:
            x, y = min(x1, x2), y1
            for i in range(abs(x1 - x2) + 1):
                field[x + i][y] += 1
        elif x2 - x1 == y2 - y1:  # diagonals
            x, y = min(x1, x2), min(y1, y2)
            for i in range(abs(x1 - x2) + 1):
                field[x + i][y + i] += 1
        elif x1 + y1 == x2 + y2:  # antidiagonals
            x, y = min(x1, x2), max(y1, y2)
            for i in range(abs(x1 - x2) + 1):
                field[x + i][y - i] += 1

    count = 0
    for row in field:
        for e in row:
            if e >= 2:
                count += 1
    return count


with open('input/input5.txt') as f:
    inp = f.read()

print(solution(inp))
