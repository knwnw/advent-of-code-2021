def solution(values: list, step: int = 1) -> int:
    count = 0
    for i in range(len(values) - step):
        if values[i + step] > values[i]:
            count += 1
    return count


with open('input/input1.txt') as f:
    values = f.read().split('\n')
    values = list(map(int, values))

print(solution(values))
print(solution(values, 3))
