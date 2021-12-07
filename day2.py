def solution1(commands: str) -> int:
    x, y = 0, 0
    for command in commands.split('\n'):
        c, val = command.split()
        if c == 'forward':
            x += int(val)
        elif c == 'down':
            y += int(val)
        elif c == 'up':
            y -= int(val)
    return x * y


def solution2(commands: str):
    x, y, aim = 0, 0, 0
    for command in commands.split('\n'):
        c, val = command.split()
        if c == 'forward':
            x += int(val)
            y += aim * int(val)
        elif c == 'down':
            aim += int(val)
        elif c == 'up':
            aim -= int(val)
    return x * y, aim


with open('input/input2.txt') as f:
    commands = f.read()

print(solution1(commands))
print(solution2(commands))
