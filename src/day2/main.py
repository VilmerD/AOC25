import math

def PrimeFactors(X):
    factors = []
    f = 1
    while f <= math.ceil(math.sqrt(X)):
        if (X % f == 0):
            factors.append(f)
            factors.append(int(X / f))
        f += 1
    return sorted(list(set(factors)))[1:]

def getNumber(string, i0):
    j = i0
    while (j < len(string) and string[j].isdigit()):
        j = j + 1
    return j

""" Reads the input and outputs the sequences as a list of tuples"""
def read_ranges(file):
    with open(file) as f:
        row = f.readline()

        " Scans forward untill next character is not a number "
        i = 0
        j = 0
        ranges = []
        while (i < len(row)):
            # Get number 
            j = getNumber(row, i)
            x0 = int(row[i:j])      

            # Skip dash
            i = j + 1           

            # Get next number
            j = getNumber(row, i)
            xe = int(row[i:j])          
            ranges.append((x0, xe))
            
            # Skip comma
            i = j + 1
        
        return ranges

def TaskA(file):
    ranges = read_ranges(file)

    sum = 0
    for r in ranges:
        print(f"{r[0]} - {r[1]}:")
        for i in range(r[0], r[1]+1):
            s = str(i)
            L = len(s)
            if (L % 2 == 0):
                L2 = int(L/2)
                if (s[:L2] == s[L2:]):
                    sum+=i

    print(f"Sum of repeated numbers: {sum}")

def ISInvalid(X):
    # Easier to check the string than the number 
    s = str(X)
    L = len(s)
    # print(f"Testing {s}")
    # Get how many divisors the length has
    factors = PrimeFactors(L)
    print(f"Size of X = {L}. Can be divided by {factors}")
    iscopy = False
    for f in factors:
        q = int(L/f)
        sub_0 = s[:q]
        # print(f"Factor = {f}, sub-sequence = {sub_0}")
        iscopy = True
        for i in range(1, f):
            sub_i = s[(i*q):((i + 1)*q)]
            # print(f"sub_i: {sub_i}")
            if (sub_i != sub_0):
                iscopy = False
                break
        if iscopy:
            # print(f"Is Copy")
            return True
    return False

def TaskB(file):
    ranges = read_ranges(file)

    sum = 0
    for r in ranges:
        print(f"Testing range [{r[0]:16d} - {r[1]:16d}]:")
        for i in range(r[0], r[1]+1):
            iscopy = ISInvalid(i)
            if iscopy:
                print(f"Invalid id {i}")
                sum += i

    print(f"Sum of repeated numbers: {sum}")

TaskB("input.txt")
