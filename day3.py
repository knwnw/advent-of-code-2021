def solution1(report: str) -> int:
    binaries = report.split()
    gamma_rate = ''
    epsilon_rate = ''
    for col in zip(*binaries):
        n_zeros = col.count('0')
        n_ones = col.count('1')
        if n_ones >= n_zeros:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def oxygen_generator_rating(report: str) -> int:
    binaries = report.split()
    n = len(binaries[0])
    i = 0
    while i < n:
        n_zeros, n_ones = 0, 0
        for b in binaries:
            if b[i] == '0':
                n_zeros += 1
            else:
                n_ones += 1
        val = '1' if n_ones >= n_zeros else '0'
        for b in binaries.copy():
            if b[i] != val:
                binaries.remove(b)
        if len(binaries) == 1:
            break
        i += 1
    return int(binaries[0], 2)


def carbon_dioxide_scrubber_rating(report: str) -> int:
    binaries = report.split()
    n = len(binaries[0])
    i = 0
    while i < n:
        n_zeros, n_ones = 0, 0
        for b in binaries:
            if b[i] == '0':
                n_zeros += 1
            else:
                n_ones += 1
        val = '1' if n_ones >= n_zeros else '0'
        for b in binaries.copy():
            if b[i] == val:
                binaries.remove(b)
        if len(binaries) == 1:
            break
        i += 1
    return int(binaries[0], 2)


def solution2(report: str) -> int:
    o2_rating = oxygen_generator_rating(report)
    co2_rating = carbon_dioxide_scrubber_rating(report)
    return o2_rating * co2_rating


with open('input/input3.txt') as f:
    report = f.read()

print(solution1(report))
print(solution2(report))
