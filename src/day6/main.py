def GetNextNum(row, j):
    i0 = j
    while(i0 < len(row) and not row[i0].isdigit()):
        i0 += 1
    ie = i0
    while (ie < len(row) and row[ie].isdigit()):
        ie += 1
    return int(row[i0:ie]), ie

def GetBlockSizes(row):
    i = 0
    I = []
    while(i < len(row)):
        if (row[i] != " "):
            I.append(i)
        i += 1
    I[-1] = I[-1] + 1
    return I

### Takes a file as input, reads it, and returns an array of numbers and a list of operations
def ReadInputA(file):
    with open(file) as f:
        lines = f.readlines() 
        ## Read numbers
        X = []
        for row in (lines[:-1]):
            x = []
            i = 0
            while (i < len(row) - 1 and row[i] != '\n'):
                xi, i = GetNextNum(row, i) 
                i += 1
                x.append(xi)
            X.append(x)
        ## Read operations
        ops = lines[-1]
        OP = []
        for c in ops.split(" "):
            if not c == "\n" and len(c) > 0:
                OP.append(c)
    return X, OP

def ReadInputB(file):
    with open(file) as f:
        lines = f.readlines() 
        nrows = len(lines) - 1
        ## Read numbers
        I = GetBlockSizes(lines[-1])
        ncols = len(I) - 1
        i0 = 0
        X = []
        for i in range(0, len(I)-1):
            i0 = I[i]
            ie = I[i+1]
            x = []
            for c in (range(ie-2, i0-1, -1)):
                chrs = []
                ## Read numbers top to bottom
                for r in range(0, nrows):
                    _x = lines[r][c]
                    if (not _x.isdigit()):
                        continue
                    chrs.append(_x)
                ## Reconstruct numbers
                xk = 0
                nchrs = len(chrs)
                for i in range(0, nchrs):
                    xk += 10 ** (nchrs - i - 1) * int(chrs[i])
                x.append(xk)
                i0 = ie
            X.append(x)
        print(X)
        ## Read operations
        ops = lines[-1]
        OP = []
        for c in ops.split(" "):
            if not c == "\n" and len(c) > 0:
                OP.append(c)
    return X, OP


def PrintResults(X, OP):
    print(X)
    print(OP)

def MakeCalculationsA(X, OP):
    ## Check num cols in X equals num cols in OP
    nop = len(OP)
    compatible = True
    for x in X:
        if not len(x) == nop:
            compatible = False
    if (compatible):
        print("Sizes compatible")
    else:
        print("Sizes not compatible")
    
    ## Iterate over columns
    Y = []
    ncol = len(OP)
    nrow = len(X)
    for c in range(0, ncol):
        op = OP[c]
        if (op == '+'):
            yk = 0
            for r in range(0, nrow):
                yk = yk + X[r][c]
        else:
            yk = 1.0
            for r in range(0, nrow):
                yk = yk * X[r][c]
        Y.append(yk)
    return Y

def MakeCalculationsB(X, OP):
    ## Iterate over columns
    Y = []
    ncol = len(OP)
    for c in range(0, ncol):
        op = OP[c]
        x = X[c]
        if (op == '+'):
            yk = 0
            for _x in x:
                yk = yk + _x
        else:
            yk = 1.0
            for _x in x:
                yk = yk * _x
        Y.append(yk)
    return Y

def TaskA():
    X, OP = ReadInputA("input.txt")
    Y = MakeCalculationsA(X, OP)
    print(f"Y = {Y}")
    sum = 0
    for yk in Y:
        sum += yk
    print(f"Sum = {sum}")

def TaskB():
    X, OP = ReadInputB("input.txt")
    Y = MakeCalculationsB(X, OP)
    print(f"Y = {Y}")
    sum = 0
    for yk in Y:
        sum += yk
    print(f"Sum = {sum}")

if __name__ == "__main__":
    ## TaskA()
    TaskB()
