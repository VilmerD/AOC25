def find_largest(row):
    i = 0
    imax = i
    vmax = 0
    while (i < len(row)):
        if (int(row[i]) > vmax):
            vmax = int(row[i])
            imax = i
        i += 1
    return imax, vmax

sum = 0
with open("input.txt") as f:
    for row in f:
        N = 12
        # Find first largest digit
        i0 = 0
        D = []
        for k in range(N-1, -1, -1):
            ie = - 1 - k
            di, d = find_largest(str(int(row[i0:ie])))
            i0 += (di + 1)
            D.append(d)
        
        jolt = 0
        for i, d in enumerate(D):
            jolt += 10**(N - 1 - i)*d
        sum += jolt

        # Print
        row_sorted = ''.join(sorted(row))
        print(f"Bank: {int(row)} -> [{jolt}] ({row_sorted[-4:]})")

print(f"Sum = {sum}")