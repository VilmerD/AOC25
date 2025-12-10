def part1(file):
    with open(file) as f:
        X = [int(line[1:]) % 100 if line[0] == "R" else (100 - int(line[1:]) % 100) for line in f]

    sum = 50
    cnt = 0
    for n in X:
        sum += n
        if (sum % 100 == 0):
            cnt = cnt + 1

    print(f"Number of zeros: {cnt}")
    print(f"Sum: {sum}")

def div(n):
    return int((n - n % 100) / 100)

def part2(file):
    sum = 50
    cnt = 0
    with open(file) as f:
        for line in f:
            A = int(line[1:])
            D = line[0]
            if (D == "R"):
                sum = sum + A
            else:
                sum = sum - A
            cnt += abs(div(sum))
            sum = sum % 100
            print(f"D = {D}, A = {A:3d}, sum = {sum:3d}, cnt = {cnt:6d}")

    print(f"Number of zeros: {cnt}")

part2("input.txt")