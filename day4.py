def solution(inp: str) -> tuple:
    pass


with open('input/input4.txt') as f:
    inp = f.read()

numbers, *boards = inp.split('\n\n')
numbers = list(map(int, numbers.split(',')))
ns = []

for n_board, board in enumerate(boards):
    d = {}
    a1, a2 = [0] * 5, [0] * 5
    for i, row in enumerate(board.split('\n')):
        for j, val in enumerate(row.split()):
            d[int(val)] = (i, j)

    count = 0
    for num in numbers:
        if num in d:
            c1, c2 = d.pop(num)
            a1[c1] += 1
            a2[c2] += 1
            count += 1
            if 5 in a1 or 5 in a2:
                break

    ns.append((count, sum(d) * num))

_, res1 = min(ns, key=lambda x: x[0])
_, res2 = max(ns, key=lambda x: x[0])

print(res1)
print(res2)
