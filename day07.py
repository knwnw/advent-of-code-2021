def solution(inp: str, part: int) -> int:
    assert part in (1, 2)

    positions = list(map(int, inp.split(',')))
    m, M = min(positions), max(positions)

    d = {}
    for i in range(m, M + 1):
        d[i] = 0
        for p in positions:
            delta = abs(p - i)
            d[i] += delta if part == 1 else (1 + delta) / 2 * delta

    res = int(min(d.values()))
    return res


with open('input/input7.txt') as f:
    inp = f.read()

print(solution(inp, part=1))
print(solution(inp, part=2))
